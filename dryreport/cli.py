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

import click
import imp
import os


@click.group()
@click.option(
    '--config',
    type=click.File(mode='r', lazy=True),
    envvar='FILE'
)
@click.pass_context
def cli(ctx, config):
    """Don't Repeat Yourself Reports"""
    filename = os.path.basename(config.name)
    basename = os.path.splitext(filename)[0]

    cfg_module = imp.new_module(basename)
    cfg_module.__file__ = filename
    try:
        exec(compile(config.read(), basename, 'exec'), cfg_module.__dict__)
    except IOError:
        ctx.fail("Unable to read configuration file.")
    except (SyntaxError, ImportError):
        ctx.fail("Unable to parse configuration file.")
    ctx.obj = cfg_module


@cli.command()
@click.pass_obj
def run(config):
    from dryreport.eval import eval_tree
    from dryreport.render import render_html
    click.echo(render_html(eval_tree(config.REPORT)))
