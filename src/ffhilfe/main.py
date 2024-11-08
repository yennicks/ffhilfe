# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse

from ffhilfe.core.executable import where_is_ffmpeg
from ffhilfe.core.processes import run_shell

ffmpeg_bin = where_is_ffmpeg()

templates = {
    "webrip": {"ffmpeg_params": ["-acodec libfdk_aac -afterburner:a 1 -vbr:a 1 -profile:a aac_low -ac 1",
                                 "-vcodec libx265 -x265-params 'crf=28:preset=slower:profile=main:level-idc=3.1'"],
               "output_format": "mkv"},
}


def parse_args():
    # this part is deprecated.
    template_names = [k for k in templates.keys()]

    parser = argparse.ArgumentParser(description="An opinionated command line ffmpeg script.")
    parser.add_argument("-c", "--concat", action="store_true",
                        help="Concatenate input files into a single output file.")
    parser.add_argument("-d", "--dry-run", action="store_true",
                        help="Show commands to be executed without executing them.")
    parser.add_argument('-t', '--template', help='The name of a predefined template', required=True)
    parser.add_argument('input', nargs='+', help='One or more input files')
    args = parser.parse_args()

    if args.template not in template_names:
        print(f"Template {args.template} not found, please one of the following: {', '.join(template_names)}")
        quit()

    return args


def output_name(input_name, output_format, concat=None):
    if concat:
        return f"output.{output_format}"

    splitted = input_name.split(".")
    assert len(splitted) > 1, f"Invalid input file name {input_name}."

    if splitted[-1] == output_format:
        splitted[-2] = splitted[-2] + "_new"
    else:
        splitted[-1] = output_format

    return ".".join(splitted)


def build_params(args):
    template = templates.get(args.template)
    batch = list()

    if args.concat:
        full_input = [f"concat|{'|'.join(args.input)}"]

    for input_name in args.input:
        full_input = input_name
        full_output = output_name(input_name, template.get('output_format'))
        command = [f'-i  "{full_input}"', *template.get('ffmpeg_params'), f'"{full_output}"']
        batch.append(command)

    return batch


def execute(ffmpeg, params, args):
    assert ffmpeg, "ffmpeg binary is not defined."
    assert params, "params are not defined."

    command = f'"{ffmpeg}" {" ".join(params)}'
    print(f"Running: {command}")
    if not args.dry_run:
        run_shell(command)

def transcode_handler(args):
    template_names = [k for k in templates.keys()]

    if args.template not in template_names:
        print(f"Template {args.template} not found, please one of the following: {', '.join(template_names)}")
        quit()

    params = build_params(args)
    for param in params:
        execute(ffmpeg_bin, param, args)


def transcode_cli(subparsers):
    parser = subparsers.add_parser('transcode', help='Transcodes from one media format to another')

    parser.add_argument("-c", "--concat", action="store_true",
                        help="Concatenate input files into a single output file.")
    parser.add_argument("-d", "--dry-run", action="store_true",
                        help="Show commands to be executed without executing them.")
    parser.add_argument('-t', '--template', help='The name of a predefined template', required=True)
    parser.add_argument('input', nargs='+', help='One or more input files')

    parser.set_defaults(func=transcode_handler)

    return parser


if __name__ == "__main__":
    args = parse_args()
