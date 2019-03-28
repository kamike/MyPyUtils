#!/usr/bin/env python
# -*- coding:utf8 -*-
from html.parser import HTMLParser
from urllib import request
import gzip

from wifi.TestCache import MyHTMLParser

# 扫描局域网可用的ip
url = 'http://192.168.'
for index in range(0, 255):
    for index2 in range(0, 255):
        ip = url + str(index) + "." + str(index2) + "/"
        # print("访问ip:" + ip)
        try:
            response = request.urlopen(ip, None, 5)
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
