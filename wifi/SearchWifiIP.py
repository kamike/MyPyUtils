#!/usr/bin/env python
# -*- coding:utf8 -*-
from concurrent.futures.thread import ThreadPoolExecutor
from urllib import request
import gzip

from utils.DiskCacheUtils import DiskCacheUtils
from bs4 import BeautifulSoup


# 扫描局域网可用的ip
class SearchWifiIP:
    def searchIp(self, url, lastI, lastJ):
        try:
            response = request.urlopen(url, None, 7)
            content = response.read()
            try:
                content = gzip.decompress(content)
            except OSError as e:
                pass
            title = self.getHtmlTitle(content)

            file = open(dir + "/ip_history.txt", "a+")

            file.write("成功访问的ip：" + url + "\tTitle：" + str(title) + "\n")
            file.flush()
            file.close()
            print("==========成功访问ip:" + url)
        except OSError as e:
            if lastJ % 50 == 0:
                print("网络超时了......" + url)
        cache.setValue("lastI", lastI)
        cache.setValue("lastJ", lastJ)

    def getHtmlTitle(self, html):
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

# currentI = 1
# currentJ = 0


url = 'http://192.168.'
print("上次进行到的ip:" + url + str(currentI) + "," + str(currentJ))
executor = ThreadPoolExecutor(max_workers=50)
search = SearchWifiIP()
for index in range(currentI, 255):
    for index2 in range(currentJ, 255):
        ip = url + str(index) + "." + str(index2)
        executor.submit(search.searchIp, ip, index, index2)
