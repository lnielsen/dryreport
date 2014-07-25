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

from birdy.twitter import UserClient


def twitter_user(screen_name, auth=None,
                 format="Twitter followers: {twitter[followers_count]}, "
                        "Tweets: {twitter[statuses_count]}"):
    def runner():
        client = UserClient(
            auth['key'],
            auth['key_secret'],
            auth['token'],
            auth['token_secret']
        )

        res = client.api.users.show.get(screen_name=screen_name)
        return format.format(twitter=res.data)
    return runner
