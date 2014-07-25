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

import github3


def commit_overview(owner, repo, branch, author=None, since=None, until=None,
                    format="{first_line} [{author}]", auth=None):
    def runner():
        gh = github3.login(**auth) if auth else github3.GitHub()
        commits = gh.repository(owner, repo).iter_commits(
            sha=branch,
            author=author,
            since=since.isoformat() if since else None,
            until=until.isoformat() if since else None,
        )

        return [
            format.format(
                commit=c,
                author=c.commit.author['name'],
                first_line=c.commit.message.splitlines()[0]
            ) for c in commits
        ]
        print(gh.ratelimit_remaining)
    return runner


def issues_overview(owner, repo, milestone=None, state=None,
                    assignee=None, mentioned=None, labels=None, sort=None,
                    since=None, format="{issue.title} [#{issue.number}]",
                    auth=None):
    def runner():
        gh = github3.login(**auth) if auth else github3.GitHub()

        issues = gh.repository(owner, repo).iter_issues(
            milestone=milestone,
            state=state,
            assignee=assignee,
            mentioned=mentioned,
            labels=",".join(labels) if labels else None,
            sort=sort,
            since=since,

        )

        return [
            format.format(
                issue=i,
            ) for i in issues
        ]
    return runner
