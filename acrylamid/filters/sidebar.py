# -*- encoding: utf-8 -*-
#
# Copyright 2016 jhammons <jhammons@saltstack.com>. All rights reserved.
# License: BSD Style, 2 clauses -- see LICENSE.
import re

from acrylamid.filters import Filter


class Sidebar(Filter):

    match = ['sidebar']
    version = 1

    priority = 60.0

    def transform(self, text, entry, *args):

        text = re.sub(r'<p>{: ?end.*? ?:}</p>', r'</div>', text)
        text = re.sub(r'<table>', r'<table class="table">', text)
        text = re.sub(r'class="sourceCode ', r'class="language-', text)
        text = re.sub(r'<img src=', r'<img class="imgcenter imgscale fifty" src=', text)
        return re.sub(r'<p>{: ?(.*?) ?:}</p>', r'<div class="\1">', text)

        #replacings = (('{% sidebar %}', open_div),
        #                ('{% end sidebar %}', close_div))
        #for k in replacings:
        #    text = text.replace(k[0], k[1])
        #return text
