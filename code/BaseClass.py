#coding=utf-8

class Father(object):
	# def __init__(self):
	# 	self.name="winda"
	# 	print "I Am Father"

	def __init__(self,name):
		self.name = name
		print "I AM FATHER :"+self.name

	def work(self,name):
		print "I word in factory"

	def __del__(self):
		print "Father Over"

class Son(Father):
	# def __init__(self):
	# 	super(Son,self).__init__()
	# 	# super(Son,self).work()
	# 	print "I Am Son"

	def __init__(self,name):
		super(Son,self).__init__(name+" . father")
		# self.name = name
		print "I AM SON :"+self.name	
		Father.work(self,"working")
		# super(Son,self).work("working")
		# self.work("programing")
		# print dir(super(Son,self))
		# print super(Son,self).__dict__
		# print super(Son,self).name
		# print Father.name

	def work(self,name):
		Father.work(self,name)
		# super(Son,self).work(name)
		# self.work("programing")		
		# print super(Son,self).name
		# super(Son,self).work()
		# super(Son,self).__del__()
		print "I work in compary" 

	def __del__(self):
		# Father.work(self,"programing")
		# super(Son,self).work("programing")
		super(Son,self).__del__()
		print "Son Over"


if __name__ == '__main__':
	# s = Son("Windard")	
	# print s.name		
	s = Son("Windard")	
	s.work("programing")
	# Father.work("working")
	# print dir(super(Son,s))
	# print super(Son,s).__name__
	# print s.name
	# s.work()

