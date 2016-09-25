#coding=utf-8

#1.0 使用print(end="")
# for i in range(100):
# 	if i%10==0:
# 		print("")
# 	print(i,end=" ")

#2.0 使用sys.stdout.write()
import sys
for i in range(100):
	if i%10==0 and i!=0:
		print("")
	sys.stdout.write(str(i)+" ")
