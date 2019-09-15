# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
from pathlib import Path
from typing import Optional

from .exception import FfhilfeException


def get_from_environment_variables(variable: str) -> Optional[Path]:
    variable = variable.upper()
    envvar = os.environ.get(variable)
    if envvar:
        return Path(envvar)
    return None


def get_from_working_directory(variable: str) -> Optional[Path]:
    if os.name == 'nt':
        variable += '.exe'
    cwd = os.getcwd()
    file = Path(cwd, variable)
    if file.exists():
        return file
    return None


def where_if_ffmpeg() -> Path:
    """
    Get the full ffmpeg executable path

    1) Environment variable
    2) Current working directory
    :return: Path
    """
    variable = 'ffmpeg'

    if get_from_environment_variables(variable):
        return get_from_environment_variables(variable)
    if get_from_working_directory(variable):
        return get_from_working_directory(variable)

    raise FfhilfeException('ffmpeg not found')
