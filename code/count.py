#coding=utf-8

def count(*args):
	num = 0
	for i in args:
		num += i
	return num

num = count(1,2,3)
print num

num = count(1,2,3,4,5,6)
print num

a = [1,2,3,4]
num = count(*a)
print num