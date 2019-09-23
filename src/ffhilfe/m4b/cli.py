# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import re
import subprocess
from pathlib import Path

from ..main import execute, ffmpeg_bin


def handler(args):
    workdir = Path.cwd()
    # print(workdir)
    # print([x for x in workdir.iterdir()])
    workfiles = [x for x in workdir.glob('*.mp3')]
    # print(workfiles)
    for w in workfiles:
        command = f'ffprobe -i "{w}" -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1'
        result = subprocess.run(command, shell=False, creationflags=subprocess.IDLE_PRIORITY_CLASS, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # print(result.stdout)
        result = str(result.stdout.decode('ascii')).splitlines()[0]
        print(int(round(float(result)*1000)))
        # result = result.split('\\n')
        # print(result)
        # result = str(result.stdout)
        # for line in result:
        #     # print(line)
        #     if line.startswith('duration='):
        #         print(line.lstrip('duration=').rstrip('\\r'))


def cli(subparsers):
    parser = subparsers.add_parser('m4b', help='Create a chapterized audiobook from one or multiple audiofiles')
    parser.add_argument('input', type=str)
    parser.set_defaults(func=handler)
    parser.set_defaults(dry_run=False)
    return parser
