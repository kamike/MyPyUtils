#!/usr/bin/env python
# -*- coding:utf8 -*-
from html.parser import HTMLParser
from urllib import request
import gzip
from urllib.error import URLError

from utils.DiskCacheUtils import DiskCacheUtils
from wifi.TestCache import MyHTMLParser
from bs4 import BeautifulSoup


def getHtmlTitle(html):
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


dir = "G:/python/temp_files"

cache = DiskCacheUtils(dir + "/cache.txt")
currentI = cache.getValue("lastI", 0)
currentJ = cache.getValue("lastJ", 0)

# 扫描局域网可用的ip
url = 'http://192.168.'
print("上次进行到的ip:" + url + str(currentI) + "," + str(currentJ))
for index in range(currentI, 255):
    cache.setValue("lastI", index)
    for index2 in range(currentJ, 255):


        ip = url + str(index) + "." + str(index2) + "/"
        # print("访问ip:" + ip)
        html = "<html></html>"
        try:
            response = request.urlopen(ip, None, 7)
            try:
                html = gzip.decompress(response.read())
            except OSError as e:
                html = response.read()
            title = getHtmlTitle(html)

            file = open(dir + "/ip_history.txt", "a+")

            file.write("成功访问的ip：" + ip + "\tTitle：" + str(title) + "\n")
            file.flush()
            file.close()
            print("==========成功访问ip:" + ip)
        except URLError as e:
            print("网络超时了......" + ip)

        cache.setValue("lastJ", index2)
