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
sdsc Module
===================

.. default-domain:: py

Checks a given DocBook XML file for stylistic errors
"""

import logging


__projectname__ = "suse-doc-style-checker"
__programname__ = "SUSE Documentation Style Checker"
__license__ = "LGPL-2.1+"
__description__ = "checks a given DocBook XML file for stylistic errors"
__authors__ = "Stefan Knorr, Thomas Schraitle, Fabian Vogt"
__url__ = "https://github.com/tomschr/sdsc"
__version__ = "2016.7.0.0"


#: Set default logging handler to avoid "No handler found" warnings.
# See https://docs.python.org/3/howto/logging.html#library-config
logging.getLogger().addHandler(logging.NullHandler())
