# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from pathlib import Path

DEFAULT_TIMEBASE = (1, 1000)


@dataclass
class Chapter:
    title: str
    start: int
    end: int
    timebase: tuple = DEFAULT_TIMEBASE


@dataclass
class Stream:
    title: str


@dataclass
class Metadata:
    title: str
    artist: str = None
    chapters: tuple = tuple()
    stream: Stream = None

    def as_ffmpeg(self):
        template_source = Path.joinpath(Path(__file__).parent, Path('metadata_template.txt'))
        with open(template_source, 'rt') as f:
            template = f.read()
        print(template)
