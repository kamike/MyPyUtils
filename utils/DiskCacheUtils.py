#!/usr/bin/env python
# -*- coding:utf8 -*-
import json

import os


class DiskCacheUtils:
    def __init__(self, cachecPath):
        if not os.path.exists(cachecPath):
            self.cacheFile = open(cachecPath, 'w');
            self.cacheFile.close()

        self.cacheFile = open(cachecPath, 'r');
        content = self.cacheFile.read()
        if content is None or content == "":
            self.dict = {}
        else:
            self.dict = json.loads(content)

    def getValue(self, key):
        if key in self.dict:
            return self.dict.get(key)
        return None

    def getValue(self, key, default):
        if key in self.dict:
            return self.dict.get(key)
        return default

    def setValue(self, key, value):
        self.dict[key] = value
        self.cacheFile = open(self.cacheFile.name, 'w');
        self.cacheFile.write(json.dumps(self.dict))
        self.cacheFile.flush()
