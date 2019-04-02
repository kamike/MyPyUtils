#!/usr/bin/env python
# -*- coding:utf8 -*-
from functools import lru_cache
from html.parser import HTMLParser

import time


class MyHTMLParser(HTMLParser):
    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=True)
        self.html_title = "null"
        self.is_title = False

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            print("==handle_starttag:" + tag)
            self.is_title = True

    def handle_endtag(self, tag):
        if tag != 'title':
            print("==handle_endtag:" + tag)
            self.is_title = False

    def handle_data(self, data):
        if (self.is_title):
            print("==handle_data:" + data)
            self.html_title = data

    def getTitile(self):
        time.sleep(1)
        return self.html_title
