# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import subprocess
import platform

def run_shell(command: str):
    match platform.system():
        case 'Windows':
            subprocess.run(command, shell=True, creationflags=subprocess.IDLE_PRIORITY_CLASS)
        case 'Darwin':
            command = f"taskpolicy -c background {command}"
            subprocess.run(command, shell=True)
        case _:
            subprocess.run(command, shell=True)
