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

from six.moves.urllib.parse import urlencode
from collections import OrderedDict as D
from datetime import datetime
import pytz

import uservoice


def to_datetime(dtstr):
    return datetime.strptime(dtstr, "%Y/%m/%d %H:%M:%S +0000").replace(
        tzinfo=pytz.utc
    )


def tickets_overview(domain, auth=None, since=None, until=None,
                     state='open', sort=None,
                     format="{ticket[subject]} "
                            "[#{ticket[ticket_number]}]"):
    def runner():
        api = uservoice.Client(
            domain,
            auth['key'],
            auth['secret'],
        ).login_as_owner()

        per_page = 100
        query = dict(per_page=per_page)

        if state:
            query['state'] = state
        if since:
            query['filter'] = 'updated_after'
            query['updated_after_date'] = since.strftime(
                "%Y-%m-%d %H:%M:%S %z"
            )

        tickets = []
        page = 1

        while True:
            query['page'] = page
            res = api.get("/api/v1/tickets.json?{0}".format(urlencode(query)))

            for t in res["tickets"]:
                if t["state"] != "deleted" and \
                   until > to_datetime(t['updated_at']):
                    tickets.append(t)

            r = res['response_data']
            if r['total_records'] < r['page']*r['per_page']:
                break
            else:
                page += 1

        return D([
            ('closed:', [
                format.format(ticket=t) for t in tickets
                if t['state'] == 'closed'
            ]),
            ('open:', [
                format.format(ticket=t) for t in tickets
                if t['state'] == 'open'
            ]),
        ])
    return runner
