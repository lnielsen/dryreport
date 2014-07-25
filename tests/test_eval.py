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

from dryreport.eval import eval_tree


class RenderTestCase(TestCase):
    def test_eval_identity(self):
        REPORT = D([
            ('key1', 'value 1'),
            ('key2', ['value 1', 'value 2']),
            ('key3', D([('key4', 'value4')])),
        ])

        expected_tree = {
            'key1': 'value 1',
            'key2': ['value 1', 'value 2'],
            'key3': {'key4': 'value4'},
        }

        self.assertEqual(
            dict(eval_tree(REPORT)),
            expected_tree,
        )

    def test_eval_callables(self):
        def fun():
            return "fun"

        def fun_list():
            return ["fun_list", "fun_list"]

        def fun_dict():
            return D([("fun_ordered_dict", "value"), ])

        REPORT = D([
            ('key1', fun),
            ('key2', ['value 1', fun_dict]),
            ('key3', D([('key4', fun_list)])),
        ])

        expected_tree = {
            'key1': 'fun',
            'key2': ['value 1', D({'fun_ordered_dict': 'value'})],
            'key3': {'key4': ['fun_list', 'fun_list']},
        }

        self.assertEqual(
            dict(eval_tree(REPORT)),
            expected_tree,
        )
