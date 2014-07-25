# -*- coding: utf-8 -*-
#
## This file is part of DRYReport.
## Copyright (C) 2014 CERN.
##
## DRYReport is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## DRYReport is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with DRYReport. If not, see <http://www.gnu.org/licenses/>.
##
## In applying this licence, CERN does not waive the privileges and immunities
## granted to it by virtue of its status as an Intergovernmental Organization
## or submit itself to any jurisdiction.

"""DRYReport (Don't Repeat Yourself Reports or Dry Reports, you choose)."""

from setuptools import setup, find_packages
import os

install_requires = [
    "github3.py>=0.8.2",
    "requests>=2.0",
    "click>=2.4",
    "six",
    "pytz",
    "uservoice",
    "birdy",
    "trello",
]

tests_require = [
    "httpretty",
    "mock",
    "nose",
    "coverage",
]

# Get the version string.  Cannot be done with import!
g = {}
with open(os.path.join("dryreport", "version.py"), "rt") as fp:
    exec(fp.read(), g)
version = g["__version__"]


setup(
    name='dryreport',
    version=version,
    url='http://github.com/lnielsen-cern/dryreport',
    license='GPLv3',
    author='CERN',
    author_email='lars.holm.nielsen@cern.ch',
    description='Research. Shared',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            "dryreport = dryreport.cli:cli",
        ]
    },
    test_suite='nose.collector',
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPLv3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
