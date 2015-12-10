#coding=utf-8
import threading

def sayhello(name):
	print "Hello I'm Thread %s" %(name)

for i in range(4):
	t = threading.Thread(target=sayhello,args=str((i+1)))
	t.start()
