# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path
import shutil

from .exception import ExecutableNotFound, FileDoesNotExist, FileExists
from .executable import get_from_anywhere
from .processes import run_shell


def where_is_mkvmerge():
    """
    Find and locate mkvmerge from the MKVToolNix package.

    :return: Path
    """
    mkvmerge = get_from_anywhere('mkvmerge')

    if isinstance(mkvmerge, Path):
        return mkvmerge

    raise ExecutableNotFound('The mkvmerge executable has not been found.')


def rewrap(src: Path, target: Path, output_format: str):
    """
    Rewrap file into a Matroska container.

    :param src: Path to the source
    :param target: Path to the target
    :param output_format: The output format, i.e. mkv
    :return:
    """
    if not src.exists():
        raise FileDoesNotExist(f'The source file does not exist. Source: {src}')

    if target.exists():
        raise FileExists(f'The target file already exists. Target: {target}')

    if output_format == 'mkv':
        mkvmerge = where_is_mkvmerge()
        command = f'"{mkvmerge}" -o "{target}" "{src}"'
        run_shell(command)
    else:
        shutil.copy(f'{src}', f'{target}')
