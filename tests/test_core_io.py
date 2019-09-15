# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import logging
import string

from ffhilfe.core.io import get_temporary_filename


def test_get_temporary_filename_is_8_3_filename_compatible():
    filename = get_temporary_filename('mkv')
    assert filename.count('.') == 1, 'Filename should have exactly one . in it.'
    assert filename.isupper(), 'All characters should be uppercase.'
    allowed_chars = set(string.ascii_uppercase + string.digits + '.')
    assert set(filename) <= allowed_chars, f'{filename} contains illegal characters.'

    a, b = filename.split('.', 1)
    assert len(a) <= 8, 'Length of first part of filename may never be longer than 8 characters.'
    assert len(b) <= 3, 'Length of extension may never be longer than 3 characters.'


def test_get_temporary_filename_gives_a_debug_message_if_extension_is_too_long(caplog):
    caplog.set_level(logging.DEBUG)
    get_temporary_filename('long')

    assert len(caplog.records) == 1
    assert '8.3 filename compatibility broken' in [text for _, _, text in caplog.record_tuples][0]
