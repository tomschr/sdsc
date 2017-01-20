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

from .app import App
from .cli import parsecli

__version__ = "2016.7.0.0"


def main(cliargs=None):
    """Entry point for the application script

    :param list cliargs: Arguments to parse or None (=use sys.argv)
    :return: return zero or non-zero value
    """
    args = parsecli(cliargs)
    app = App(args)
    print(args)
    print(app)
    print(app.xsltfiles)
    print(app.parser)
    return 0
