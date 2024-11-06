# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import subprocess
import sys

def run_shell(command: str):
    if sys.platform.startswith('win'):
        subprocess.run(command, shell=True, creationflags=subprocess.IDLE_PRIORITY_CLASS)
    else:
        subprocess.run(command, shell=True)
