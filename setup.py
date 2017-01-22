#!/usr/bin/env python
# -*- encoding: utf-8 -*-
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


import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

PROJECTNAME = "suse-doc-style-checker"
PROGRAMNAME = "SUSE Documentation Style Checker"


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name=PROJECTNAME,
    version='2016.7.0.0',
    license='LGPL-2.1+',
    description='Style Checker for SUSE Documentation',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Stefan Knorr, Thomas Schraitle',
    author_email='sknorr@suse.de',
    url='https://github.com/openSUSE/suse-doc-style-checker',

    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        # Indicate who your project is intended for
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Intended Audience :: Developers'
        #
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        #
        'Operating System :: Unix',
        'Operating System :: POSIX',
        # 'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],

    keywords=["docbook5", "style", "style-checking"],

    install_requires=[
        'lxml', 'docopt',
    ],
    tests_require=['pytest'],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    entry_points={
        'console_scripts': [
            'sdsc = sdsc.cli:main',
        ]
    },
)
