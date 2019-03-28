#!/usr/bin/env python
#-*- coding:utf8 -*-
from wifi.TestCache import MyHTMLParser

parser = MyHTMLParser()
parser.feed('<html><head><title>Test22222222</title></head>'
            '<body><h1>Parse me!</h1><img src = "" />'
            '<!-- comment --></body></html>')
print("===========")
print(parser.getTitile())