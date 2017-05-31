#
# Copyright (c) 2017 SUSE Linux GmbH
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 3 of the GNU General Public License as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, contact SUSE LLC.
#
# To contact SUSE about this file by physical or electronic mail,
# you may find current contact information at www.suse.com

from unittest.mock import MagicMock, Mock
from multiprocessing import Pool
import pytest

from sdsc.stylecheck import CleanExit, getstylechecks, singlestylecheck


def test_getstylechecks():
    assert getstylechecks()


def test_singlestylecheck():
    assert singlestylecheck("fake-style", "fake.xml")


def test_cleanexit():
    pool = MagicMock(spec=Pool)
    pool.terminate = Mock(return_value=None)
    pool.join = Mock(return_value = None)

    with CleanExit(pool):
        raise KeyboardInterrupt

    assert pool.terminate.called
    assert pool.join.called
