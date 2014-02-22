############################
#	2013-1-10
#	Name:Doubanpa
#	Author:Lazynight
#	Blog:lazynight.me
#	Version:0.1
############################

import re,urllib,urllib2,cookielib
import cookies

def getsource(url):
    cookie_jar = cookies.cookies()
    opener = cookie_jar.opener()
    urllib2.install_opener(opener)

    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows;U;Windows NT 5.1;zh-CN;rv:1.9.2.9)Gecko/20100824Firefox/3.6.9')
        source = urllib2.urlopen(req).read()
        source = source.replace("'", "''");
        return source

    except Exception,e:
        print "====exception===",str(e)

