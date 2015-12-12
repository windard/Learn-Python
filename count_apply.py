#coding=utf-8

def count(*args):
	num = 0
	for i in args:
		num += i
	return num

num = apply(count,[1,2,3])
print num

a = [1,2,3,4,5,6]
num = apply(count,a)
print num

