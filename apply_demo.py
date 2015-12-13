#coding=utf-8

def a(func,args):
	return func(*args)

def count(*args):
  num = 0
  for i in args:
    num += i
  return num

num = a(count,[1,2,3])
print num

a = [1,2,3,4,5,6]
# num = a(count,a)
print num	