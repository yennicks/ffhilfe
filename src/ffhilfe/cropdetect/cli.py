# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from ..main import execute, ffmpeg_bin


def handler(args):
    params = [f'-i {args.input}',
              f'-t 1',
              f'-vf cropdetect',
              f'-f null -']
    execute(ffmpeg_bin, params, args)


def cli(subparsers):
    parser = subparsers.add_parser('cropdetect')
    parser.add_argument('input', type=str)
    parser.set_defaults(func=handler)
    parser.set_defaults(dry_run=False)
    return parser
