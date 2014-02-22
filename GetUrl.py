#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################
#   2013-1-10
#   Name:Doubanpa
#   Author:Lazynight
#   Blog:lazynight.me
#   Version:0.1
############################

import BeautifulSoup
import re

#提取网页中符合格式的链接

def GetUrl(strPage):

    urllist = []
    try:
        content = BeautifulSoup.BeautifulSoup(strPage).findAll('a')
    except:
        content = ''


    pat = re.compile(r'href="([^"]*)"')
    pat2 = re.compile(r'^http://music.douban.com/subject/\d+/$')
    for item in content:
        h = pat.search(str(item))
        if h is not None:
            href = h.group(1)
        if pat2.search(href):
            urllist.append(href)
    return urllist