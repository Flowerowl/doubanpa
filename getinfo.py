############################
#	2013-1-10
#	Name:Doubanpa
#	Author:Lazynight
#	Blog:lazynight.me
#	Version:0.1
############################

import urllib,re,Image
import simplejson as json
import database
import source
from BeautifulSoup import BeautifulSoup as bs

#通过api，但是有访问次数限制
def getdata(url):

	#打分百分比
	scores,genre = getdatahtml(url)
	print genre

	index = url.index('subject')
	length = len(url)
	url = 'https://api.douban.com/v2/music/'+url[index+8:length]

	music_url = source.getsource(url)
	jsondata = json.loads(music_url)

	#打分
	#rating_max = jsondata['rating']['max']
	rating_average = jsondata['rating']['average']
	rating_numraters = jsondata['rating']['numRaters']
	#rating_min = jsondata['rating']['min']
	#专辑信息
	try:
		artist = jsondata['author'][0]['name'].replace("'","''").replace('-','_')
	except:
		artist = ''
	#封面地址
	cover = jsondata['image']
	index = cover.index('spic')
	length = len(cover)
	cover = cover[0:index]+'lpic'+cover[index+4:length]
	#标题
	title = jsondata['title'].replace("'","''").replace('-','_')
	#专辑id
	id = jsondata['id']
	#简介
	try:
		summary = jsondata['summary'].replace("'","''").replace('-','_')
	except:
		summary = ''
	try:
	#出版商
		publisher = jsondata['attrs']['publisher'][0].replace("'","''").replace('-','_')
	except:
		publisher = ''
	try:
	#版本特性
		version = jsondata['attrs']['version'][0]
	except:
		version = ''
	#发行时间
	try:
		pubdate = jsondata['attrs']['pubdate'][0]
	except:
		pubdate = ''
	try:
	#介质
		media = jsondata['attrs']['media'][0].replace("'","''").replace('-','_')
	except:
		media = ''
	try:
	#唱片数
		discs = jsondata['attrs']['discs'][0]
	except:
		discs = ''
	#曲目
	tracks = ''
	try:
		songs = jsondata['attrs']['songs']
		for i in songs:
			tracks += i['title'].replace("'","''").replace('-','_')+';'
	except:
		tracks = ''
	#标签
	try:
		tags =  jsondata['tags']
	except:
		tags = ''
	#print id, title ,artist ,genre, pubdate, publisher, discs, media, version, summary, tracks, tags
	# try:
	# 	database.insert(id,title,artist,genre,pubdate,publisher,discs,\
	# 		media,version,summary,rating_average,tracks,tags,rating_numraters,scores)
	# 	downimg(cover,id)
	# except:
	#  	print id+'is bad'
	database.insert(int(id),title,artist,genre,pubdate,publisher,discs,media,version,summary,float(rating_average),tracks,tags,rating_numraters,scores)
	downimg(cover,id)
	#database.insert(id,title,artist,genre,pubdate,publisher,discs,isbn,media,version,summary,rating_average,tracks,tags,rating_numraters,scores)
	print id,title


#通过分析source，有限制但是可以通过cookie变换来抵消
def getdatahtml(url):
	#打分
	s = source.getsource(url)
	content = bs(s).findAll('div',attrs={'id':'interest_sectl'})
	pat = re.compile(r'([0-9.]+)*%')
	h = pat.findall(str(content))
	#流派
	genre = ''
	content = bs(s).findAll('div',attrs={'id':'info'})
	pat = re.compile(ur'流派:</span>&nbsp;\S*')
	result = pat.findall(str(content).decode('utf8'))
	if len(result) != 0:
		g = result[0]
		length = len(g)
		index = g.index('&nbsp;')
		genre = g[index+6:length]

	return h,genre


#下载图片失败，记录
def downimg(imgurl,id):
	try:
		urllib.urlretrieve(imgurl,'/z/ilbumfm/fm/static/cover/'+id+'.jpg')
		img = Image.open('/z/ilbumfm/fm/static/cover/'+id+'.jpg')
		width = int(300)
		(x,y) = img.size
		height =int( y * width /x)
		small_img =img.resize((width,height),Image.ANTIALIAS)
		small_img.save('/z/ilbumfm/fm/static/cover/'+id+'.jpg')

		width = int(140)
		(x,y) = img.size
		height =int( y * width /x)
		small_img =img.resize((width,height),Image.ANTIALIAS)
		small_img.save('/z/ilbumfm/fm/static/scover/'+id+'.jpg')
	except:
		logfile = file('#logimg.txt','w')
		logfile.write(id+'\n')
		logfile.close()

