import sqlite3
import urllib
con = sqlite3.connect('/z/ilbumfm/doubanpa/douban.db')
cur = con.cursor()
cur.execute("select id from album")
result_list = []
for row in cur.fetchall():
    t = int(row[0])
    result_list.append(t)
new_list = result_list[169058:]
for id in new_list:
	try:
		urllib.urlretrieve('http://img3.douban.com/lpic/s'+str(id)+'.jpg','/z/ilbumfm/doubanpa/img/'+str(id)+'.jpg')
		print str(id)+' is OK'
	except:
		logfile = file('#logimg.txt','w')
		logfile.write(str(id)+'\n')
		logfile.close()
