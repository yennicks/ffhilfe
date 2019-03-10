#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import subprocess


ffmpeg_bin = 'ffmpeg'
templates = {
    "webrip": {"ffmpeg_params": ["-acodec libfdk_aac -afterburner:a 1 -vbr:a 1 -profile:a aac_low -ac 1",
                                 "-vcodec libx265 -x265-params 'crf=28:preset=slower:profile=main:level-idc=3.1'"],
               "output_format": "mkv"}
}


def parse_args():
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


def output_name(input_name, output_format):
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

    for input_name in args.input:
        full_input = input_name
        full_output = output_name(input_name, template.get('output_format'))
        command = [f"-i  {full_input}", *template.get('ffmpeg_params'), full_output]
        batch.append(command)

    return batch


def execute(ffmpeg: str = ffmpeg_bin, params: list = None, args = None):
    assert ffmpeg, "ffmpeg binary is not defined."
    assert params, "params are not defined."

    command = f"{ffmpeg} {' '.join(params)}"
    print(f"Running: {command}")
    if not args.dry_run:
        subprocess.run(command, shell=True)


if __name__ == "__main__":
    args = parse_args()
    params = build_params(args)
    for param in params:
        execute(ffmpeg_bin, param, args)
