# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
from pathlib import Path

from ffhilfe.core.executable import where_is_ffmpeg
from ffhilfe.core.io import get_temporary_file
from ffhilfe.core.matroska import rewrap
from .helpers import output_file
from .settings import get_settings
from ..core.processes import run_shell


def process(file: Path):
    print(file.absolute())

    output_format = get_settings(file).get('output_format', 'mkv')

    parameters = get_settings(file).get('parameters')
    parameters_pass_1 = get_settings(file).get('parameters_pass_1')
    parameters_pass_2 = get_settings(file).get('parameters_pass_2')

    if parameters:
        print('Using parameters: ', parameters)
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
    elif parameters_pass_1 and parameters_pass_2:
        print('Using parameters pass 1: ', parameters_pass_1)
        print('Using parameters pass 2: ', parameters_pass_2)
        tmp_target = get_temporary_file(output_format)
        target = output_file(file)
        command_1 = [
            f'"{where_is_ffmpeg().absolute()}"',
            f'-y -i "{file.absolute()}"',
            parameters_pass_1,
            f'-pass 1 -an -f null /dev/null',
        ]
        command_1 = ' '.join(command_1)
        run_shell(command_1)
        command_2 = [
            f'"{where_is_ffmpeg().absolute()}"',
            f'-i "{file.absolute()}"',
            parameters_pass_2,
            f'-pass 2 "{tmp_target.absolute()}"',
        ]
        command_2 = ' '.join(command_2)
        run_shell(command_2)
        rewrap(tmp_target, target, output_format)

        os.remove(tmp_target)
    else:
        print('Not Implemented.')
