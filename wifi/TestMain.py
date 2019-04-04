#!/usr/bin/env python
# -*- coding:utf8 -*-
import gzip
from urllib import request
from urllib.error import HTTPError, URLError

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from bs4 import BeautifulSoup

from wifi.TestCache import MyHTMLParser


def getHtmlTitle(html):
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.title.string
    except AttributeError as e:
        return None
    return title


respond = request.urlopen("http://192.168.1.240", None, 7)
html = respond.read()
print(html)
print(getHtmlTitle(html))
