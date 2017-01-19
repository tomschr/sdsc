========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |coveralls| |codecov|
        | |landscape| |scrutinizer|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/suse-doc-style-checker/badge/?style=flat
    :target: https://readthedocs.org/projects/suse-doc-style-checker
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/openSUSE/suse-doc-style-checker.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/openSUSE/suse-doc-style-checker

.. |coveralls| image:: https://coveralls.io/repos/openSUSE/suse-doc-style-checker/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/openSUSE/suse-doc-style-checker

.. |codecov| image:: https://codecov.io/github/openSUSE/suse-doc-style-checker/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/openSUSE/suse-doc-style-checker

.. |landscape| image:: https://landscape.io/github/openSUSE/suse-doc-style-checker/master/landscape.svg?style=flat
    :target: https://landscape.io/github/openSUSE/suse-doc-style-checker/master
    :alt: Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/sdsc.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/sdsc

.. |downloads| image:: https://img.shields.io/pypi/dm/sdsc.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/sdsc

.. |wheel| image:: https://img.shields.io/pypi/wheel/sdsc.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/sdsc

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/sdsc.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/sdsc

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/sdsc.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/sdsc

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/openSUSE/suse-doc-style-checker/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/openSUSE/suse-doc-style-checker/


.. end-badges

Style Checker for SUSE Documentation

* Free software: BSD license

Installation
============

::

    pip install sdsc

Documentation
=============

https://suse-doc-style-checker.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
