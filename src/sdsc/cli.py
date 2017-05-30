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

"""Checks a given DocBook XML file for stylistic errors

Usage:
    sdsc [-h | --help]
    sdsc [-v ...] [options] XMLFILES...

Required Arguments:
    XMLFILES          Path to one or more XML files to style check

Options:
    -h, --help        Shows this help
    -v                Raise verbosity level
    --version         Prints the version
    -j <N>, --jobs=<N>
                      Allow N jobs at once [default: {cpu}]
    --output=<OUTFILE>, -o <OUTFILE>
                      Optional file where results are written to
    -s, --show        show final report in $BROWSER, or default browser if
                      unset; not all browsers open report files correctly and
                      for some users, a text editor will open; in such cases,
                      set the BROWSER variable with: export BROWSER=/MY/BROWSER
                      Chromium or Firefox will both do the right thing
    --module          writes name of current check module to stdout
    --checkpatterns   check formal validity of built-in regular expression
                      patterns
"""


from docopt import docopt, DocoptExit
import logging
from logging.config import dictConfig
from multiprocessing import cpu_count


from .common import (DEFAULT_LOGGING_DICT,
                     CPU_FACTOR,
                     LOGLEVELS,
                     )
from .stylecheck import process


#: Use __package__, not __name__ here to set overall logging level:
log = logging.getLogger(__package__)


def parsecli(cliargs=None):
    """Parse CLI arguments with docopt

    :param list cliargs: List of commandline arguments
    :return: dictionary from docopt
    :rtype: dict
    """
    from sdsc import __version__
    version = "%s %s" % (__package__, __version__)
    args = docopt(__doc__.format(cpu=cpu_count() * CPU_FACTOR),
                  argv=cliargs, version=version)
    dictConfig(DEFAULT_LOGGING_DICT)
    log.setLevel(LOGLEVELS.get(args['-v'], logging.DEBUG))

    log.debug("CLI result: %s", args)
    return args


def checkargs(args):
    """Check arguments

    :param args: dictionary from docopt parsing
    """
    log.debug("Checking arguments")
    try:
        args['--jobs'] = int(args['--jobs']) * CPU_FACTOR
    except ValueError:
        raise DocoptExit("The --jobs option does not contain "
                         "an integer value (got %r)" % args['--jobs'])
    log.debug("Checking successful")


def main(cliargs=None):
    """Entry point for the application script

    :param list cliargs: Arguments to parse or None (=use sys.argv)
    :return: return codes from ``ERROR_CODES``
    """

    try:
        args = parsecli(cliargs)
        checkargs(args)
        result = process(args)
        log.info("Done.")
        return result

    except KeyboardInterrupt:
        return 10
