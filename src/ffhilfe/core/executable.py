# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
from pathlib import Path
from typing import Optional

from .exception import ExecutableNotFound


def get_from_environment_variables(executable: str) -> Optional[Path]:
    executable = executable.upper()
    envvar = os.environ.get(executable)
    if envvar:
        return Path(envvar)
    return None


def get_from_working_directory(executable: str) -> Optional[Path]:
    if os.name == 'nt':
        executable += '.exe'
    cwd = os.getcwd()
    file = Path(cwd, executable)
    if file.exists():
        return file
    return None


def get_from_anywhere(executable: str) -> Optional[Path]:
    """
    Try to get the executable from anywhere.

    Use the following search pattern:
    1) Environment variable
    2) Current working directory

    :param executable: str
    :return: Optional[Path]
    """

    if get_from_environment_variables(executable):
        return get_from_environment_variables(executable)
    if get_from_working_directory(executable):
        return get_from_working_directory(executable)

    return None


def where_is_ffmpeg() -> Path:
    """
    Get the full ffmpeg executable path

    :return: Path
    """
    ffmpeg = get_from_anywhere('ffmpeg')

    if isinstance(ffmpeg, Path):
        return ffmpeg

    raise ExecutableNotFound('The ffmpeg executable has not been found')
