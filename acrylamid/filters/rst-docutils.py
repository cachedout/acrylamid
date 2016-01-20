# -*- encoding: utf-8 -*-
#
# Copyright 2012 Martin Zimmermann <info@posativ.org>. All rights reserved.
# License: BSD Style, 2 clauses -- see LICENSE.
#
# This file is the original rst plugin, but was renamed in this build
# in favor of my version of rst.py which uses Pandoc.

import sys
import os
import imp
import traceback

from acrylamid import log
from acrylamid.filters import Filter, discover

try:
    from docutils.core import publish_parts
    from docutils.parsers.rst import roles, directives
except ImportError:
    publish_parts = roles = directives = None  # NOQA


class RestructuredtextDocutils(Filter):

    match = ['rst-docutils']
    version = 2

    conflicts = ['markdown', 'plain', 'rst']
    priority = 70.00

    def init(self, conf, env):

        self.extensions = {}
        self.ignore = env.options.ignore

        if not publish_parts or not directives:
            raise ImportError('reStructuredText: No module named docutils')

        # -- discover reStructuredText extensions --
        directories = conf['filters_dir'] + [os.path.dirname(__file__)]
        for filename in discover(directories, lambda path: path.startswith('rstx_')):
            modname, ext = os.path.splitext(os.path.basename(filename))
            fp, path, descr = imp.find_module(modname, directories)

            try:
                mod = imp.load_module(modname, fp, path, descr)
                mod.register(roles, directives)
            except (ImportError, Exception) as e:
                traceback.print_exc(file=sys.stdout)
                log.warn('%r %s: %s' % (filename, e.__class__.__name__, e))

    def transform(self, content, entry, *filters):

        settings = {
            'initial_header_level': 1,
            'doctitle_xform': 0,
            'strip-elements-with-classes': 'section'
        }
        if isinstance(content, dict):
            blocks = {}
            for key, value in content.iteritems():
                blocks[key] = publish_parts(value, writer_name='html', settings_overrides=settings)
            return blocks
        else:
            parts = publish_parts(content, writer_name='html', settings_overrides=settings)
            return parts['body']
