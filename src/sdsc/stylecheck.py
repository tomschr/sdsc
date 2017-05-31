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
from multiprocessing import Pool, Process, Queue, JoinableQueue, current_process
import glob
import random
import time
import os
import signal

from .common import XSLCHECKPATH

log = logging.getLogger(__name__)



class CleanExit(object):
     def __enter__(self):
             return self
     def __exit__(self, exc_type, exc_value, exc_tb):
         if exc_type is KeyboardInterrupt:
             return True
         return exc_type is None



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
    jobname = current_process().name
    log.info("%s %s", style, xmlfile)
    log.debug("[%s] Style check %r with %r", jobname, xmlfile, os.path.basename(style))
    # Simulate a hard working function, sleep for 0..4s
    sleep = random.randint(0, 20)/10
    time.sleep(sleep)
    return (xmlfile, style, sleep)


def stylepool_x(xmlfiles, styles, jobs=None):
    """Create a multiprocessing pool distributed on jobs

    :param xmlfiles: list of XML files
    :param styles: list of styles to apply to each XML file
    :param jobs: integer to allow N jobs at once; None defaults to CPU count
    :return: tuple of result
    """
    #with Pool(jobs, init_worker) as pool:
    #    try:
    #        values = pool.starmap(func=singlestylecheck,
    #                              iterable=itertools.product(styles, xmlfiles))
    #        # pool.close() # close the process pool
    #    except ExitProcessError:
    #        log.error("Canceled.")
    #        values = [None]
    #    except KeyboardInterrupt:
    #        log.fatal("Received ^C, aborting")
    #        pool.terminate()
    #        pool.join()
    # ------------------------------------------
    job_queue = Queue()
    result_queue = Queue()

    for data in itertools.product(styles, xmlfiles):
        job_queue.put(data)

    workers = []
    for i in range(jobs):
        p = Process(target=singlestylecheck,
                    args=(i, job_queue, result_queue))
        p.start()
        workers.append(p)

    try:
        for process in workers:
            process.join()
    except KeyboardInterrupt:
        log.error("Keyboard interrupt in stylepool")
        for process in workers:
            process.terminate()
            process.join()
        raise

    values = []
    while not result_queue.empty():
        values.append(result_queue.get(block=False))
    return values


def stylepool(xmlfiles, styles, jobs=None):
    """Create a multiprocessing pool distributed on jobs

    :param xmlfiles: list of XML files
    :param styles: list of styles to apply to each XML file
    :param jobs: integer to allow N jobs at once; None defaults to CPU count
    :return: tuple of result
    """
    def init_worker():
        # Catch all ^C from child processes
        signal.signal(signal.SIGINT, signal.SIG_IGN)

    with Pool(jobs, init_worker) as pool:
        try:
            values = pool.starmap(func=singlestylecheck,
                                  iterable=itertools.product(styles, xmlfiles))
            pool.close()
        except KeyboardInterrupt:
            log.fatal("Received ^C, aborting")
            # Not sure how to avoid that:
            pool.terminate()
            pool.join()
            values = None

    return values


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

    log.info("process ended %.3fs", end - start)
    log.info("End result: %s", results)
    return 0
