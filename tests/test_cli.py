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
  (['in.xml', 'out.xml'],
   {'INPUTFILE': 'in.xml',
    'OUTPUFILE': 'out.xml'}
   ),
  (['-v', 'in.xml', 'out.xml'],
   {'-v': 1,
    'INPUTFILE': 'in.xml',
    'OUTPUFILE': 'out.xml'}
   ),
  (['-vv', 'in.xml', 'out.xml'],
   {'-v': 2,
    'INPUTFILE': 'in.xml',
    'OUTPUFILE': 'out.xml'}
   ),
  (['-vvv', 'in.xml', 'out.xml' ],
   {'-v': 3,
    'INPUTFILE': 'in.xml',
    'OUTPUFILE': 'out.xml'}
   ),
  #(['--report', 'report.svrl', '--schema', 'schema.sch', 'a.xml'],
   #{'--report': 'report.svrl',
    #'--schema': 'schema.sch',
    #'XMLFILE':  'a.xml'}
   #),
   #(['--phase', 'foo', '--schema', 'schema.sch', 'a.xml'],
   #{'--phase': 'foo',
    #'--schema': 'schema.sch',
    #'XMLFILE':  'a.xml'}
   #),
])
def test_parsecli(cli, expected):
    result = parsecli(cli)
    # Create set difference and only compare this with the expected dictionary
    assert {item: result.get(item, None) for item in expected} == expected


