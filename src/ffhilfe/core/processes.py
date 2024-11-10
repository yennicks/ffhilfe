# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import enum
import os
import subprocess
import platform

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

def _run_macos(command, priority):
    """
    Run a command a macOS (Darwin)
    """
    if priority is Priorities.NORMAL:
        subprocess.run(command, shell=True)
    elif priority is Priorities.IDLE:
        command = f"taskpolicy -c background {command}"
        subprocess.run(command, shell=True)
    else:
        raise ImplementationError('Requested priority noy implemented.')

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


def run_shell(command: str):
    priority = Priorities.IDLE
    print('Running command:', command)
    match platform.system():
        case 'Windows':
            _run_windows(command, priority)
        case 'Darwin':
            _run_macos(command, priority)
        case _:
            _run_unix(command, priority)
