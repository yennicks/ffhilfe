# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path

from ffhilfe.core.executable import get_from_environment_variables


def test_get_ffmpeg_from_environment_variables_in_windows(monkeypatch):
    variable = 'ffmpeg'

    monkeypatch.setenv('FFMPEG', 'C:\\ffmpeg.exe')
    ffmpeg = get_from_environment_variables(variable)
    assert isinstance(ffmpeg, Path)

    monkeypatch.delenv('FFMPEG')
    ffmpeg = get_from_environment_variables(variable)
    assert ffmpeg is None
