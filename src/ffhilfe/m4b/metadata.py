# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


@dataclass
class Chapter:
    timebase: tuple = (1, 1000)
    start: int
    end: int
    title: str


@dataclass
class Stream:
    title: str


@dataclass
class Metadata:
    title: str
    artist: str
