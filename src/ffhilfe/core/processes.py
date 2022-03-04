# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import enum
import os
import subprocess
import platform
from sys import platform

from ffhilfe.core.exception import ImplementationError


class Priorities(enum.Enum):
    IDLE = enum.auto()
    NORMAL = enum.auto()


def _run_windows(command, priority):
    """
    Run a command a Windows OS
    """
    if priority is Priorities.NORMAL:
        priority_class = subprocess.NORMAL_PRIORITY_CLASS
    elif priority is Priorities.IDLE:
        priority_class = subprocess.IDLE_PRIORITY_CLASS
    else:
        raise ImplementationError('Requested priority noy implemented.')

    subprocess.run(command, shell=True, creationflags=priority_class)


def run_shell(command: str):
    match platform.system():
        case 'Windows':
            subprocess.run(command, shell=True, creationflags=subprocess.IDLE_PRIORITY_CLASS)
        case 'Darwin':
            command = f"taskpolicy -c background {command}"
            subprocess.run(command, shell=True)
        case _:
            subprocess.run(command, shell=True)
def _run_unix(command, priority):
    """
    Run a command a Unix-like OS
    """
    if priority is Priorities.NORMAL:
        priority_nice = None
    elif priority is Priorities.IDLE:
        priority_nice = 19
    else:
        raise ImplementationError('Requested priority noy implemented.')

    if priority_nice:
        subprocess.run(command, shell=True, preexec_fn=lambda: os.nice(priority_nice))
    else:
        subprocess.run(command, shell=True)


def _run(command, priority):
    """
    Run a command
    """
    if platform == "win32":
        _run_windows(command, priority)
    else:
        _run_unix(command, priority)


def run_idle(command: str) -> None:
    """
    Run a command with lowest priority
    """
    _run(command, Priorities.IDLE)
