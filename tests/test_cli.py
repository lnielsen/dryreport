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

from __future__ import absolute_import, print_function, unicode_literals

from click.testing import CliRunner
from dryreport.cli import cli


def test_cli():
    runner = CliRunner()

    ## Skip test
    #with runner.isolated_filesystem():
    #    with open('report.py', 'w') as f:
    #        f.write("pass")
    #    result = runner.invoke(cli, ['--config', 'report.py', ])
    #    assert result.exit_code == -1

    result = runner.invoke(cli, ['--config', 'missing.py', 'run'])
    assert result.exit_code != 0


def test_cli_error():
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open('report.py', 'w') as f:
            f.write("REPORT \;= []")
        result = runner.invoke(cli, ['--config', 'report.py', 'run'])
        assert result.exit_code != 0

        with open('report2.py', 'w') as f:
            f.write("raise ImportError()")
        result = runner.invoke(cli, ['--config', 'report2.py', 'run'])
        assert result.exit_code != 0
