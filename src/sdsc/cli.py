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

"""
Usage:
   sdsc [-h | --help]
   sdsc  [-v ...] [options] INPUTFILE [OUTPUTFILE]

checks a given DocBook XML file for stylistic errors

Positional Arguments:
  INPUTFILE          DocBook XML file to check
  OUTPUTFILE         optional result XML file; if not give, use stdout

Options:
  -h, --help         show this help message and exit
  --version          show version number and exit
  -b, --bookmarklet  open Web page that lets you install a bookmarklet to
                     manage style checker results
  -s, --show         show final report in $BROWSER, or default browser if
                     unset; not all browsers open report files correctly and
                     for some users, a text editor will open; in such cases,
                     set the BROWSER variable with: export BROWSER=/MY/BROWSER
                     ; Chromium or Firefox will both do the right thing
  --module           writes name of current check module to stdout
  --performance      write performance measurements to stdout
  --checkpatterns    check formal validity of built-in regular expression
                     patterns
"""

#
#Module that contains the command line app.
#
#Why does this file exist, and why not put this in __main__?
#
#  You might be tempted to import things from __main__ later, but that will cause
#  problems: the code will get executed twice:
#
#  - When you run `python -msdsc` python will execute
#    ``__main__.py`` as a script. That means there won't be any
#    ``sdsc.__main__`` in ``sys.modules``.
#  - When you import __main__ it will get executed again (as a module) because
#    there's no ``sdsc.__main__`` in ``sys.modules``.
#
#  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
#

from docopt import docopt


def parsecli(cliargs=None):
    from sdsc import __version__
    version = "%s %s" % (__package__, __version__)
    args = docopt(__doc__, argv=cliargs, version=version)
    return args
