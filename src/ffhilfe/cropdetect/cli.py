# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from ..main import execute
from ffhilfe.core.executable import where_is_ffmpeg


def handler(args):
    params = [f'-i "{args.input}"',
              f'-t 5',
              f'-vf "cropdetect=20:2:20"',
              f'-f null -']
    execute(where_is_ffmpeg(), params, args)


def cli(subparsers):
    parser = subparsers.add_parser('cropdetect', help='Detects the cropping of black borders for a transcode')
    parser.add_argument('input', type=str)
    parser.set_defaults(func=handler)
    parser.set_defaults(dry_run=False)
    return parser
