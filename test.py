# import sqlite3
# con = sqlite3.connect('/z/ilbumfm/doubanpa/douban.db')
# cur = con.cursor()
# id =1
# title,artist,genre,pubdate,publisher,discs,media,version,summary,tracks,tags= '','','','','','','','','','',''
# # cur.execute("insert into album values('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%f')" % \
# # 				(id,title,artist,genre,pubdate,publisher,discs,media,version, summary,tracks,'',11.6))
# cur.execute("SELECT average FROM score WHERE id='%s'" % 1394541)
# con.commit()
# average = cur.fetchone()
# print average[0]
import os
print os.path
