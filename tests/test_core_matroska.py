# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from unittest.mock import patch
from pathlib import Path

from ffhilfe.core.matroska import rewrap


class PathExists(Path):
    """
    Mocked Path class.
    """
    # _flavour = Path()._flavour  # Hack so that Path allows to subclass itself.

    def exists(self) -> bool:
        return True


class PathDoesNotExist(Path):
    """
    Mocked Path class.
    """
    # _flavour = Path()._flavour  # Hack so that Path allows to subclass itself.

    def exists(self) -> bool:
        return False


def test_rewrap(monkeypatch):
    src = PathExists('/sourcefile.mkv')
    target = PathDoesNotExist('/targetfile.mkv')

    with patch('ffhilfe.core.matroska.where_is_mkvmerge'), patch('subprocess.run'):
        rewrap(src, target)
