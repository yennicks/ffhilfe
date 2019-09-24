# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path
from typing import Optional
import yaml
from ffhilfe.core.exception import IsNotAFile, SettingsNotFound


def get_from_file_name(src: str) -> Optional[Path]:
    stem = src.stem
    settings_name = f'{stem}.ff'
    directory = src.parent
    settings_file = directory.joinpath(settings_name)

    if settings_file.exists():
        return settings_file

    return None


def get_from_directory(src: str) -> Optional[Path]:
    stem = src.stem
    directory = src.parent

    possibilities = [
        'ffhilfe',
        'ffhilfe_1',
        'ffhilfe_2',
        'ffhilfe_3',
        'ffhilfe_4',
        'ffhilfe_5',
    ]

    for possibility in possibilities:
        settings_name = f'{possibility}.ff'
        settings_file = directory.joinpath(settings_name)
        if settings_file.exists():
            return settings_file

    return None


def where_is_settings_file(src: Path) -> Path:
    if not src.is_file():
        raise IsNotAFile('An input file was expected.')

    directory = src.parent
    assert directory.is_dir(), 'This should be a directory.'

    # 1: file name
    if get_from_file_name(src):
        return get_from_file_name(src)
    if get_from_directory(src):
        return get_from_directory(src)

    raise SettingsNotFound('No valid settings file was found.')


def get_settings(src: Path):
    settings_file = where_is_settings_file(src)
    with open(settings_file, 'r') as o:
        settings = yaml.safe_load(o)
    return settings
