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

from unittest import TestCase
from collections import OrderedDict as D
from dryreport import render


class RenderTestCase(TestCase):
    def test_render_text(self):
        data = D([
            ('Key 1', [
                D([
                    ('Key 2', ['Value 1', 'Value 2']),
                ]),
                'Value 3',
            ]),
            ('Key 3', 'Value 4'),
        ])

        res = """- Key 1
    - Key 2
        - Value 1
        - Value 2
    - Value 3
- Key 3
    - Value 4
"""
        self.assertEqual(
            render.render_text(data),
            res
        )
