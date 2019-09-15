# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import subprocess
from pathlib import Path

from .exception import ExecutableNotFound, FileDoesNotExist, FileExists
from .executable import get_from_anywhere


def where_is_mkvmerge():
    """
    Find and locate mkvmerge from the MKVToolNix package.

    :return: Path
    """
    mkvmerge = get_from_anywhere('mkvmerge')

    if isinstance(mkvmerge, Path):
        return mkvmerge

    raise ExecutableNotFound('The mkvmerge executable has not been found.')


def rewrap(src: Path, target: Path):
    """
    Rewrap file into a Matroska container.

    :param src: Path to the source
    :param target: Path to the target
    :return:
    """
    if not src.exists():
        raise FileDoesNotExist(f'The source file does not exist. Source: {src}')

    if target.exists():
        raise FileExists(f'The target file already exists. Target: {target}')

    mkvmerge = where_is_mkvmerge()

    command = f'{mkvmerge} -o {target} {src}'
    subprocess.run(command, shell=True, creationflags=subprocess.IDLE_PRIORITY_CLASS)
