DRYReport
=========

Don't Repeat Yourself Reports or alternatively Dry Reports (you choose).

DRYReport is a small commandline client for generating periodic reports by pulling 
information from GitHub, UserVoice, Trello and Twitter so you don't have to copy/paste
from all the sources where the information is already typed once.


Installation
============
::

    $ pip install https://github.com/lnielsen-cern/dryreport.git


Usage
=====

Create a report config file::

    #
    # report.py
    #
    
    from collections import OrderedDict as D
    from datetime import datetime, timedelta
    import pytz

    from dryreport.contrib.github import commit_overview, issues_overview
    from dryreport.contrib.uservoice import tickets_overview
    from dryreport.contrib.twitter import twitter_user
    from dryreport.contrib.trello import cards_overview


    until = datetime.now(pytz.utc)
    since = until - timedelta(days=7)

    github_auth = dict(
        username='CHANGEME',
        password='CHANGEME',
    )

    uservoice_auth = dict(
        key='CHANGEME',
        secret='CHANGEME',
    )

    twitter_auth = dict(
        key="CHANGEME",
        key_secret="CHANGEME",
        token="CHANGEME",
        token_secret="CHANGEME",
    )

    trello_auth = dict(
        key='CHANGEME',
        # Get a token via:
        # from trello import TrelloApi
        # TrelloApi(key).get_token_url('App', expires='never', write_access=False)
        token='CHANGEME',
    )

    commit_args = dict(
        since=since,
        until=until,
        author='your@email',
        auth=github_auth,
    )


    # Report defined in a variable called REPORT
    REPORT = D([
        # Get all open cards from the list "Done" in the board id 1234567
        ("Trello:", cards_overview('1234567', 'Done', auth=trello_auth)),
        ("Twitter:", [
            twitter_user('zenodo_org', auth=twitter_auth),
        ]),
        ("GitHub:", D([
            # Get all commits to GitHub repository branch by author
            ("invenio@pu:", commit_overview(
                "owner", "repo", "branch",
                **commit_args
            )),
            ("RFCs:", issues_overview(
                "owner",
                "repo",
                since=since,
                labels=["RFC"],
                auth=github_auth,
            )),
        ])),
        ("UserVoice Support", tickets_overview(
            "YOURDOMAIN", auth=uservoice_auth,
            since=since, until=until
        )),
    ])


Run the report with::

  $ dryreport --config report.py run

Tests
=====
::

    $ python setup.py test


License
=======
Copyright (C) 2014 CERN.

DRYReport is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

DRYReport is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with DRYReport. If not, see <http://www.gnu.org/licenses/>.

In applying this licence, CERN does not waive the privileges and immunities
granted to it by virtue of its status as an Intergovernmental Organization
or submit itself to any jurisdiction.
