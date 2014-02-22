import urllib,re,sqlite3
from BeautifulSoup import BeautifulSoup as bs
import source

con = sqlite3.connect('/z/ilbumfm/ilbumfm/db/douban.db')
cur = con.cursor()
cur.execute("select id, title, artist from album where xiaid is NULL")# 
idlist = []
titlelist = []
artistlist = []
for douban in cur.fetchall():
	idlist.append(douban[0])
	titlelist.append(douban[1].encode('utf-8'))
	artistlist.append(douban[2].encode('utf-8'))
for i in range(len(titlelist)):
	url = "http://www.xiami.com/search/album?key="+titlelist[i].replace(' ','+')+'+'+artistlist[i].replace(' ','+')
	# url='http://www.xiami.com/search/album?key='
	# url = 'http://www.xiami.com/search/album?key=%E5%91%A8%E6%9D%B0%E4%BC%A6'
	xiasource = source.getsource(url)
	content = bs(xiasource).find('a',attrs={'class':'CDcover100'})
	if type(content)==None:
		url = "http://www.xiami.com/search/album?key="+titlelist[i].replace(' ','+')
		xiasource = source.getsource(url)
		content = bs(xiasource).find('a',attrs={'class':'CDcover100'})
	pat = re.compile(r'/album/\d+')
	h = pat.findall(str(content))
	if h:
		h = h[0]
		xiaid = h[7:]
		cur.execute('UPDATE album SET xiaid = %s WHERE id = %d' % (xiaid, idlist[i]))
		con.commit()
		print idlist[i],titlelist[i],artistlist[i], xiaid
cur.close()
con.close()




