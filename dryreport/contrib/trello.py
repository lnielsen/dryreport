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

from trello import TrelloApi


def cards_overview(board_id, list_name, auth=None, format="{card[name]}"):
    def runner():
        trello = TrelloApi(auth['key'], token=auth['token'])

        # Get list id
        list_id = None
        res = trello.boards.get_list(board_id)
        for r in res:
            if r['name'] == list_name:
                list_id = r['id']
                break

        # Get cards
        if list_id:
            res = trello.lists.get(list_id, cards='open')
            return [
                format.format(
                    card=c,
                ) for c in res['cards']
            ]
        return ["Trello ERROR"]
    return runner
