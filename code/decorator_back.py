#coding=utf-8

from time import ctime,sleep

def timefun(func):
	def showtime():
		print ctime()
		return func
	return showtime()

@timefun
def foo():
	print "This is foo"

for i in range(3):
	foo()
	sleep(2)

print "-"*20
timefun(foo)

print "-"*20
timefun(foo)()
