# -*- encoding: utf-8 -*-
#
# License: This document has been placed in the public domain
# Author: Jacob Hammons

import re
import pypandoc

from acrylamid.filters import Filter

class RstPandocTabs(Filter):

    match = ['rst-tabs']
    version = 1

    conflicts = ['rst', 'plain']
    priority = 70.0

    def transform(self, text, entry, *filters):

        pattern = re.compile(r'\.\. ?\[\[ ?(.*?) ?\]\] ?\{#?(.*?)\} ?')
        tab_matches = pattern.findall(text)
        text = re.sub(r'\.\. ?\[\[ ?(.*?) ?\]\] ?\{#?(.*?)\} ?', r'{TABBULLETS}\n\n.. raw:: html\n\n\t<div id="\2" class="tab-pane fade in active">\n\n', text, 1)
        text = re.sub(r'\.\. ?\[\[ ?(.*?) ?\]\] ?\{#?(.*?)\} ?', r'.. raw:: html\n\n\t</div><div id="\2" class="tab-pane fade in">\n\n', text)
        tab_bullets = '.. raw:: html\n\n\t<ul class="nav nav-tabs">\n'

        for idx, tab_match in enumerate(tab_matches):

            if idx == 0:
                tab_bullets += '\t<li class="active"><a data-toggle="tab" href="#' + tab_match[1] + '">' + tab_match[0] + '</a></li>\n'
            else:
                tab_bullets += '\t<li><a data-toggle="tab" href="#' + tab_match[1] + '">' + tab_match[0] + '</a></li>\n'

        tab_bullets += '\t</ul>\n\t<div class="tab-content">'
        text += "\n\n.. raw:: html\n\n\t</div>\n\n"

        text = re.sub(r'{TABBULLETS}', tab_bullets, text)


        return pypandoc.convert(text, 'html', format='rst')
