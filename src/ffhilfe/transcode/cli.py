# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from argparse import ArgumentParser
from pathlib import Path
from .main import process


def handler(args):
    for file in args.input:
        src = Path(file)
        process(src)


def cli(subparsers) -> ArgumentParser:
    parser = subparsers.add_parser('transcode', help='Transcodes from one media format to another')

    parser.add_argument('input', nargs='+', help='One or more input files')

    parser.set_defaults(func=handler)

    return parser
