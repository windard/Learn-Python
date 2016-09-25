#coding=utf-8

from random import randint

def odd(n):
	return n%2

allNum = []

for i in range(10):
	allNum.append(randint(1,99))

print filter(odd,allNum)