import os, glob, urllib, re
import Image
path = '/z/ilbumfm/fm/static/cover'
width =int(140)
imgslist = glob.glob(path+'/*.jpg')
format = '.jpg'
def small_img():
    for imgs in imgslist:
      try:
        imgspath, ext = os.path.splitext(imgs)
        imgspath = imgspath.replace('cover','scover')
        img = Image.open(imgs)
        (x,y) = img.size
        height =int( y * width /x)
        small_img =img.resize((width,height),Image.ANTIALIAS)
        small_img.save(imgspath + format)
        print imgspath+' is OK.'
      except:
          pat = re.compile('\d+')
          h = pat.search(imgspath)
          id = h.group()
          urllib.urlretrieve("http://img3.douban.com/lpic/s"+ id +".jpg",'/z/ilbumfm/fm/static/cover/'+id+'.jpg')
    print 'done'
if __name__ == '__main__':
    small_img()