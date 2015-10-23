# import urllib2  
# response = urllib2.urlopen('http://www.baidu.com/')  
# html = response.read()  
# print html 

import urllib2    
req = urllib2.Request('http://www.baidu.com')    
response = urllib2.urlopen(req)    
the_page = response.read()   
# try:
data_file = open('baidu.html','w')
for each in the_page:
	data_file.write(each)
data_file.close()

# except:
# 	print "This is is an ERROR" 
# print the_page  