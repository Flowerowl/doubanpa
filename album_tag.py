import sqlite3

con = sqlite3.connect('/z/ilbumfm/doubanpa/douban.db')
cu = con.cursor()
cu.execute("SELECT id FROM album")
albumidlist=[]
for albumid in cu.fetchall():
  albumidlist.append(albumid[0])
taglist = ''
#albumidlist = albumidlist[5716:]
for albumid in albumidlist:
  cu.execute('SELECT t.name FROM album_tag at, tag t, album a WHERE a.id = at.albumid AND t.tagid = at.tagid AND a.id=%d AND a.id > "%d"' %(albumid, 1403488))
  for tag in cu.fetchall():
    t=tag[0].encode('utf-8')
    t=t.replace("'","''")
    t=t.replace("-","")
    taglist+=t+';'
  print taglist
  try:
    cu.execute('UPDATE album SET tags = "%s" where id = "%d"' %(taglist,albumid))
    con.commit()
  except:
    None
  taglist=''

  # AND id > "%d"