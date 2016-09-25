#coding=utf-8

#1.0 在print后面加上,
# for i in range(100):
# 	if i%10==0 and i!=0:
# 		print "\n"
# 	print i,

#2.0 使用sys.stdout.write()
import sys
for i in range(100):
	if i%10==0 and i!=0:
		print "\n"
	sys.stdout.write(str(i)+" ")
