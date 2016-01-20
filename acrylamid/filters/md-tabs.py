# -*- encoding: utf-8 -*-
#
# License: This document has been placed in the public domain
# Author: Jacob Hammons

import re
import pypandoc

from acrylamid.filters import Filter


class Tabs(Filter):

    match = ['md-tabs']
    conflicts = ['rst', 'plain', 'md']
    version = 1

    priority = 70.0

    def transform(self, text, entry, *args):

        pattern = re.compile(r'<!-- ?\[\[ ?(.*?) ?\]\] ?\{#?(.*?)\} ?-->')
        tab_matches = pattern.findall(text)
        text = re.sub(r'<!-- ?\[\[ ?(.*?) ?\]\] ?\{#?(.*?)\} ?-->', r'{TABBULLETS}\n<div id="\2" class="tab-pane fade in active">\n', text, 1)
        text = re.sub(r'<!-- ?\[\[ ?(.*?) ?\]\] ?\{#?(.*?)\} ?-->', r'</div><div id="\2" class="tab-pane fade in">\n', text)
        tab_bullets = '<ul class="nav nav-tabs">\n'

        for idx, tab_match in enumerate(tab_matches):

            if idx == 0:
                tab_bullets += '<li class="active"><a data-toggle="tab" href="#' + tab_match[1] + '">' + tab_match[0] + '</a></li>\n'
            else:
                tab_bullets += '<li><a data-toggle="tab" href="#' + tab_match[1] + '">' + tab_match[0] + '</a></li>\n'

        tab_bullets += '</ul>\n\n<div class="tab-content">'
        text += "\n</div>\n"
        text = re.sub(r'{TABBULLETS}', tab_bullets, text)
        return pypandoc.convert(text, 'html', format='markdown+pipe_tables',extra_args=['--highlight-style=zenburn','--smart'])
