#!/usr/bin/env python
# -*- coding:utf8 -*-
from utils.DiskCacheUtils import DiskCacheUtils

cache = DiskCacheUtils("G:/python/temp_files/cache.txt")
# cache.setValue("aaa", "11111")
# cache.setValue("bbbbbbb", "22222222")
print(cache.getValue("aaa"))
print(cache.getValue("bbbbbbb"))
print(cache.getValue("bbbbb"))
