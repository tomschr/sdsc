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

from logging import (BASIC_FORMAT,
                     CRITICAL,
                     DEBUG,
                     FATAL,
                     ERROR,
                     INFO,
                     NOTSET,
                     WARN,
                     WARNING,
                     )
from lxml.etree import (QName,
                        XMLSyntaxError,
                        XSLTApplyError,
                        XSLTParseError,
                        )
import os


# Error codes
# Make an error dictionary that contains both the class and its
# string representation
ERROR_CODES = dict()
for _error, _rc in [(XMLSyntaxError, 20),
                    (XSLTApplyError, 20),
                    (XSLTParseError, 30),
                    (FileNotFoundError, 40),
                    (OSError, 40),
                    ]:
    ERROR_CODES[_error] = _rc
    ERROR_CODES[repr(_error)] = _rc


def errorcode(error):
    """Get the error exit code from an exception ``error``

    :param error: exception instance
    :return: exit code
    :rtype: int
    """
    return ERROR_CODES.get(repr(type(error)), 255)


#: Paths to all *.xslc files
XSLCHECKPATH=os.path.join(os.path.dirname(__file__), "xsl-checks")

#: Prefix to namespace mappings
NSMAP = dict(db="http://docbook.org/ns/docbook",
             )

#: Factor to multiply with multiprocessing.cpu_count() function:
CPU_FACTOR = 2

#: Map verbosity to log levels
LOGLEVELS = {None: WARNING,  # 0
             0: WARNING,
             1: INFO,
             2: DEBUG,
             }

#: Map log numbers to log names
LOGNAMES = {NOTSET: 'NOTSET',      # 0
            None: 'NOTSET',
            DEBUG: 'DEBUG',        # 10
            INFO: 'INFO',          # 20
            WARN: 'WARNING',       # 30
            WARNING: 'WARNING',    # 30
            ERROR: 'ERROR',        # 40
            CRITICAL: 'CRITICAL',  # 50
            FATAL: 'CRITICAL',     # 50
            }


#: Default logging dict for :class:`logging.config.dictConfig`:
DEFAULT_LOGGING_DICT = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            # See https://docs.python.org/3.5/library/logging.html#logrecord-attributes
            'format': '[%(levelname)s] %(name)s::%(funcName)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'NOTSET',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            # 'stream': 'ext://sys.stderr',
        },
    },
    'loggers': {
        'sdsc': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        }
    }
}
