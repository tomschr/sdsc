#
# Copyright (c) 2016 SUSE Linux GmbH
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


import pytest
from sdsc.cli import parsecli


@pytest.mark.parametrize('cli,expected', [
  (['-o', 'out.xml', 'in.xml'],
   {'XMLFILES': ['in.xml'],
    '--output': 'out.xml'}
   ),
  (['-o', 'out.xml', 'inA.xml', 'inB.xml'],
   {'XMLFILES': ['inA.xml', 'inB.xml'],
    '--output': 'out.xml'}
   ),
  (['-v', '-o', 'out.xml', 'in.xml'],
   {'-v': 1,
    'XMLFILES': ['in.xml'],
    '--output': 'out.xml'}
   ),
  (['-vv', '-o', 'out.xml', 'in.xml'],
   {'-v': 2,
    'XMLFILES': ['in.xml'],
    '--output': 'out.xml'}
   ),
  (['-vvv', '-o', 'out.xml', 'in.xml',],
   {'-v': 3,
    'XMLFILES': ['in.xml'],
    '--output': 'out.xml'}
   ),
])
def test_parsecli(cli, expected):
    result = parsecli(cli)
    # Create set difference and only compare this with the expected dictionary
    assert {item: result.get(item, None) for item in expected} == expected


