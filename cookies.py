############################
#	2013-1-10
#	Name:Doubanpa
#	Author:Lazynight
#	Blog:lazynight.me
#	Version:0.1
############################

import urllib,cookielib,urllib2,sqlite3,StringIO,json,os,time

class cookies:
    def __init__(self):
        self.domain = 'douban.com'
        self.path = r'/z/ilbumfm/doubanpa/cookies.db'
        self.jspath = r'/z/ilbumfm/doubanpa/sessionstore.js'

#构造cookie
    def opener(self):
        # con = sqlite3.connect(self.path)
        # con.text_factory = str
        # cur = con.cursor()
        #cur.execute("select host, path, isSecure, expiry, name, value from moz_cookies where host like ?",['%%%s%%' % self.domain])
        ftstr = ["FALSE","TRUE"]
        s = StringIO.StringIO()
        s.write('# Netscape HTTP Cookie File\n')
        s.write('# http://www.netscape.com/newsref/std/cookie_spec.html\n')
        s.write('# This is a generated file!  Do not edit\n')
        #cooklist = douban cookie在cookies.db中的数据
        for item in cooklist:
            s.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (
                item[0], ftstr[item[0].startswith('.')], item[1],
                ftstr[item[2]], item[3], item[4], item[5]))

        if os.path.exists(self.jspath):
            try:
                js_data = json.loads(open(self.jspath, 'rb').read())
            except Exception, e:
                print str(e)
            else:
                if 'windows' in js_data:
                    for window in js_data['windows']:
                        for cookie in window['cookies']:
                            s.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (cookie.get('host', ''), ftstr[cookie.get('host', '').startswith('.')], \
                                     cookie.get('path', ''), False, str(int(time.time()) + 3600*24*7), cookie.get('name', ''), cookie.get('value', '')))
        s.seek(0)
        cookie_jar = cookielib.MozillaCookieJar()
        cookie_jar._really_load(s, '', True, True)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
        # cur.close()
        # con.close()
        return opener

# cookies = cookies()
# opener = cookies.opener()
# print opener
