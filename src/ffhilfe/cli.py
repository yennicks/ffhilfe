# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from .main import build_params, execute, ffmpeg_bin, parse_args


def cli():
    args = parse_args()
    params = build_params(args)
    for param in params:
        execute(ffmpeg_bin, param, args)
