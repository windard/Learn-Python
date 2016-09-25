#coding=utf-8

def echo(**arge):
	for (i,j) in arge.items():
		print i,j

echo(a="one",b="two")

#此处的键值不能为数字,必须为是一个变量
# echo(1="one",2="two")

echo(**{"1":"one","2":"two","3":"three"})

#此处的键值也不能为数字，必须是字符串
# echo(**{1:"one",2:"two",3:"three"})
