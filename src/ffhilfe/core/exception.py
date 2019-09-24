# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


class FfhilfeException(Exception):
    pass


class ExecutableNotFound(FfhilfeException):
    pass


class FileDoesNotExist(FfhilfeException):
    pass


class FileExists(FfhilfeException):
    pass


class IsNotAFile(FfhilfeException):
    pass


class SettingsNotFound(FfhilfeException):
    pass
