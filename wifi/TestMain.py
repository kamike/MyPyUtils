#!/usr/bin/env python
# -*- coding:utf8 -*-
import gzip
from urllib import request
from urllib.error import HTTPError, URLError

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import sys
from bs4 import BeautifulSoup

from wifi.TestCache import MyHTMLParser

path=sys.path[0]

print(path)
print(path.index('\\',len(path)-5,len(path)))
