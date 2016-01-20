# -*- encoding: utf-8 -*-
#
# License: This document has been placed in the public domain
# Author: Jacob Hammons

import pypandoc


from acrylamid.filters import Filter

class MdPandoc(Filter):

    match = ['md', 'mkdown', 'markdown', 'Markdown']
    version = 1

    conflicts = ['rst', 'plain']
    priority = 70.0

    def transform(self, text, entry, *filters):

        return pypandoc.convert(text, 'html', format='markdown+pipe_tables+backtick_code_blocks', extra_args=['--smart'])
