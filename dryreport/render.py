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

from collections import OrderedDict
import six


def format_line(text, prefix='- ', indent=0, indent_char=' '):
    return indent_char*indent + prefix + text + "\n"


def render_text(subtree, level=0):
    if isinstance(subtree, six.text_type):
        return format_line(subtree, indent=level*4)
    elif isinstance(subtree, OrderedDict):
        out = ""
        for key, value in subtree.items():
            out += format_line(key, indent=level*4)
            out += render_text(value, level=level+1)
        return out
    elif isinstance(subtree, list):
        out = ""
        for item in subtree:
            out += render_text(item, level=level)
        return out


def render_html(subtree, level=0):
    if isinstance(subtree, six.text_type):
        return "<li>{0}</li>\n".format(subtree)
    elif isinstance(subtree, OrderedDict):
        out = ""
        for key, value in subtree.items():
            out += "<li>{0} <ul>".format(key)
            out += render_html(value, level=level+1)
            out += "</ul>"
        return out
    elif isinstance(subtree, list):
        out = ""
        for item in subtree:
            out += render_html(item, level=level)
        return out
