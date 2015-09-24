
#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
#    http://pic.meizitu.com/wp-content/uploads/2015a/09/27/01.jpg
#    reg = r'src="(.+\.jpg)"'
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1


html = getHtml("http://www.meizitu.com/a/5104.html")

print getImg(html)