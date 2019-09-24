# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path
from .settings import get_settings


def output_name(file: Path) -> str:
    stem = file.stem
    output_format = get_settings(file).get('output_format')
    return f'{stem}.{output_format}'


def output_file(file: Path) -> Path:
    directory = file.parent
    return directory.joinpath(output_name(file))
