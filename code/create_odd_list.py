#coding=utf-8

from random import randint

allNum = []

for i in range(10):
	allNum.append(randint(1,99))

print [n for n in allNum if n%2]