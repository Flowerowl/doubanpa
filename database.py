#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################
#	2013-1-10
#	Name:Doubanpa
#	Author:Lazynight
#	Blog:lazynight.me
#	Version:0.1
############################

import sqlite3
import simplejson as json

def insert(id,title,artist,genre,pubdate,publisher,discs,media,version,summary,average,tracks,tags,rating_numraters,scores):

	try:
		con = sqlite3.connect('/z/ilbumfm/ilbumfm/db/douban.db')
		cur = con.cursor()
		#values = [id,title,artist,genre,pubdate,publisher,discs,isbn,media,version,summary,average]
		cur.execute("select * from album where id = '%d'" % id )
		row = cur.fetchone()
		if not row:
			cur.execute("insert into album values('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%f',NULL)" % \
					(id,title,artist,genre,pubdate,publisher,discs,media,version,summary,tracks,'',average))
			con.commit()
	
			cur.execute("insert into score values('%d','%f','%f','%f','%f','%f','%f','%f')" \
				% (id,float(scores[0]),float(scores[1]),float(scores[2]),float(scores[3]),float(scores[4]),float(average),float(rating_numraters)))
			con.commit()
	
			if len(tags) != 0:
				taglist = ''
				for i in tags:
					t = i['name'].encode('utf-8')
					t=t.replace("'","''")
					t=t.replace("-","_")
					taglist+=t+';'
					cur.execute("select tagid from tag where name ='%s'" % t)
					con.commit()
					row = cur.fetchone()
					if not row:
						#NULL，自增id
						cur.execute("insert into tag values(NULL,'%s')" % t )
						con.commit()
					cur.execute("select tagid from tag where name = '%s'" % t)
					tagid = cur.fetchone()
					tagid = tagid[0]
					cur.execute("insert into album_tag values('%d','%d','%d')" % (id,tagid,int(i['count'])))
					con.commit()
				cur.execute("update album set tags ='%s' where id = '%d' " % (taglist, id))
				con.commit()
	
		else:
			print 'Already exist'
	
		cur.close()
		con.close()
	except sqlite3.OperationalError, why:
		print "sqlite3 error:%s\n" % str(why)
# try:


	# except sqlite3.OperationalError, why:
	# 	print "sqlite3 error:%s\n" % str(why)
