#coding=utf-8
import urllib
import json
from pprint import pprint
url = "http://api.kzhihu.com/userdetail2/1f644a1b7da169d2b56e1a4c6da61fea"
page = urllib.urlopen(url)
html = page.read()
data = json.loads(html)
# pprint(data)
for i in range(len(data["topanswers"])):
	print data["topanswers"][i]["link"]
	print data["topanswers"][i]["title"]
# thing = u"\u7a0b\u6d69\uff0c\u751f\u65e5\u5feb\u4e50"
# print thing.encode("gbk")
