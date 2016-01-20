# -*- encoding: utf-8 -*-
#
# License: This document has been placed in the public domain
# Author: Jacob Hammons

import re
import pypandoc

from acrylamid.filters import Filter

class RstPandoc(Filter):

    match = ['restructuredtext', 'rst', 'rest', 'reST', 'reStructuredText']
    version = 1

    conflicts = ['rst', 'plain']
    priority = 70.0

    def transform(self, text, entry, *filters):

        return pypandoc.convert(text, 'html', format='rst')
