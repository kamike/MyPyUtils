#!/usr/bin/env python
# -*- coding:utf8 -*-
from html.parser import HTMLParser
from urllib import request
import gzip

from utils.DiskCacheUtils import DiskCacheUtils
from wifi.TestCache import MyHTMLParser

cache = DiskCacheUtils("G:/python/temp_files/cache.txt")
currentI = cache.getValue("lastI", 0)
currentJ = cache.getValue("lastJ", 0)

# 扫描局域网可用的ip
url = 'http://192.168.'
print("上次进行到的ip:" + url + str(currentI) + "," + str(currentJ))
for index in range(currentI, 255):
    cache.setValue("lastI", index)
    for index2 in range(currentJ, 255):
        cache.setValue("lastJ", index2)

        ip = url + str(index) + "." + str(index2) + "/"
        # print("访问ip:" + ip)
        try:
            response = request.urlopen(ip, None, 3)
            html = gzip.decompress(response.read())
            parser = MyHTMLParser()
            print(html)
            parser.feed(str(html))

            file = open("G:/python/temp_files/ip_history.txt", "a+")

            file.write("成功访问的ip：" + ip + "\tTitle：" + parser.getTitile() + "\n")
            file.flush()
            file.close()
            print("==========成功访问ip:" + ip)
        except OSError as e:
            print("网络超时了......" + ip)
