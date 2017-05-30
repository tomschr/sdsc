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

import itertools
import logging
from multiprocessing import Pool, Queue, JoinableQueue, cpu_count
import glob
import random
import time
import os

from .common import XSLCHECKPATH

log = logging.getLogger(__name__)


def getstylechecks():
    """Return a list of all .xslc files

    :return: style check files (.xslc)
    """
    return glob.glob(os.path.join(XSLCHECKPATH, "*.xslc"))


def singlestylecheck(style, xmlfile):
    """Perform a single stylecheck

    :param data: tuple of styles and XML files
    :return: tuple of a single entry; an entry contains XML file, style, and the result
    """
    # style, xmlfile = data
    log.debug("Style check %r with %r", xmlfile, os.path.basename(style))
    # Simulate a hard working function, sleep for 0..4s
    sleep = random.randint(0, 20)/10
    time.sleep(sleep)
    log.debug("  stylesingle returns: %s", sleep)
    return (xmlfile, style, sleep)


def stylepool(xmlfiles, styles, jobs=None):
    """Create a multiprocessing pool distributed on jobs

    :param xmlfiles: list of XML files
    :param styles: list of styles to apply to each XML file
    :param jobs: integer to allow N jobs at once; None defaults to CPU count
    :return: tuple of result
    """
    pool = Pool(jobs)
    try:
        values = pool.starmap(func=singlestylecheck,
                              iterable=itertools.product(styles, xmlfiles))
        pool.close() # close the process pool
        return values
    except KeyboardInterrupt:
        log.error("Canceled.")
        return None


def process(args):
    """Process the style check

    :param dict args: Dictionary of parsed CLI arguments
    :return: return exit value
    :rtype: int
    """
    log.debug("Now in process()")
    start = time.time()
    results = stylepool(xmlfiles=args['XMLFILES'],
                        styles=getstylechecks(),
                        jobs=args['--jobs'])
    end = time.time()

    log.debug("process ended %.3fs", end - start)
    log.debug("End result: %s", results)
    return 0
