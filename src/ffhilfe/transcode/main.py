# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
from pathlib import Path
import subprocess
from ffhilfe.core.executable import where_is_ffmpeg
from ffhilfe.core.io import get_temporary_file
from ffhilfe.core.matroska import rewrap
from .helpers import output_file
from .settings import get_settings
from ..core.processes import run_shell


def process(file: Path):
    print(file.absolute())

    parameters = get_settings(file).get('parameters')
    output_format = get_settings(file).get('output_format', 'mkv')
    assert parameters, 'cant be none!'
    print(parameters)
    tmp_target = get_temporary_file(output_format)
    target = output_file(file)
    command = [
        f'"{where_is_ffmpeg().absolute()}"',
        f'-i "{file.absolute()}"',
        parameters,
        f'"{tmp_target.absolute()}"',
    ]
    command = ' '. join(command)
    run_shell(command)
    rewrap(tmp_target, target, output_format)

    os.remove(tmp_target)
