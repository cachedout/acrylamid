# -*- encoding: utf-8 -*-
#
# Copyright 2016 jhammons <jhammons@saltstack.com>. All rights reserved.
# License: BSD Style, 2 clauses -- see LICENSE.
import re

from acrylamid.filters import Filter


class Cards(Filter):

    match = ['cards']
    version = 1

    priority = 60.0

    def transform(self, text, entry, *args):

        text = re.sub(r'<!-- ?card ?-->', r'\n<div class="col-sm-6 col-md-4 col-lg-2">\n', text)
        return re.sub(r'<!-- ?end.*?-->', r'\n</div>\n', text)
