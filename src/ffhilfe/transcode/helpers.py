# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path
from ffhilfe.core.exception import FileExists
from .settings import get_settings

def output_name(file: Path) -> str:
    stem = file.stem
    output_format = get_settings(file).get('output_format')
    yield f'{stem}.{output_format}'
    for i in range(999):
        i = str(i).zfill(3)
        yield f'{stem}_{i}.{output_format}'


def output_file(file: Path) -> Path:
    directory = file.parent
    for o in output_name(file):
        target = directory.joinpath(o)
        if not target.exists():
            return target

    raise FileExists('Could not create a valid output file because the filename is not unique.')
