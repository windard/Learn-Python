#coding=utf-8

def static(func):
	def count(*args):
		count._call += 1
		print count._call
		func(*args)
	count._call = 0
	return count

#在非递归调用中完全可以当做静态变量来使用
@static
def echo():
	pass

for i in range(5):
	echo()

#但是在递归调用中就出问题
# @decorator
# def fin(x):
# 	if x<2: return 1
# 	return (fin(x-1)+fin(x-2))

# print fin(5)
