#!/usr/bin/env python
# -*- coding:utf8 -*-
import gzip
from urllib import request
from urllib.error import HTTPError, URLError

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from bs4 import BeautifulSoup

from wifi.TestCache import MyHTMLParser


def dosmothing():
    print("dosmothing......")
    time.sleep(2)


executor = ThreadPoolExecutor(max_workers=3)
for index in range(10):
    executor.submit(dosmothing)

print("end...")
