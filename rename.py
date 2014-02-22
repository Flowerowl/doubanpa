import os,sys,random

dir = '/z/ilbumfm/fm/static/cover'
filenames = os.listdir(dir)

for name in xrange(len(filenames)):
	id = int(filenames[name].split('.')[0])
	changed_id = int((id+6393)*7+12390753)
	os.rename(dir+os.sep+filenames[name],dir+os.sep+str(changed_id)+'.jpg')