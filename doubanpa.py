#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#	2013-1-10
#	Name:Doubanpa
#	Author:Lazynight
#	Blog:lazynight.me
#	Version:0.1
#

import engine

url = raw_input('Setting your url (-->http://www.baidu.com)\n')
thNumber = int(raw_input('Setting the thread number:'))
isDFS = bool(raw_input('1 or '':'))

wc = engine.WebCrawler(thNumber)
wc.CrawStyle(url, isDFS)

