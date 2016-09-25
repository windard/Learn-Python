# class A:
#     def __init__(self):
#         self.namea="aaa"
#     def funca(self):
#         print "function a : %s"%self.namea
# class B(A):
#     def __init__(self):
#         self.nameb="bbb"
#     def funcb(self):
#         print "function b : %s"%self.nameb
# b=B()
# print b.nameb
# b.funcb()
# b.funca()

# class MyException(Exception):                                          
# 	message = "An unknown exception occurred."                           
# 	code =500                                                         
# 	headers = {}                                                      
# 	safe =False                                                       
# 	def __init__(self, message=None):            
# 		if not message:                                
# 			message =self.message           	                         
# 		super(MyException,self).__init__(message)   
# exc  = MyException('help')  
# print exc.message  
# print super(MyException, exc).message  
# s = Exception("hehe")
# print s.message

# class Father(object):

# 	def __init__(self,name):
# 		self.name = name
# 		print "I AM FATHER :"+self.name
# 		self.work("Working")

# 	def work(self,name):
# 		# self.workname = name
# 		print "I word in factory",self.name

# 	def __del__(self):
# 		print "Father Over"

# class Son(Father):

# 	def __init__(self,name):
# 		super(Son,self).__init__(name+" . father")
# 		self.name = name
# 		# print "I AM SON :"+self.name	
# 		super(Son,self).work("Working")
# 		self.work("Programing")

# 	def work(self,name):
# 		Father.work(self,name)
# 		print "I work in compary",name 

# 	def __del__(self):
# 		super(Son,self).__del__()
# 		print "Son Over"

# if __name__ == '__main__':
# 	s = Son("Windard")	
# 	super(Son,s).work("Working")
# 	# print s.work

# class Father(object):

# 	def __init__(self,name):
# 		self.name = name
# 		self.__work("Working")
# 		# print "I AM FATHER :"+self.name

# 	def __work(self,name):
# 		print "My name is :",self.name
# 		print "I word in factory",name

# 	def __del__(self):
# 		# self.work("Working")
# 		print "Father Over"

# class Son(Father):

# 	def __init__(self,name):
# 		super(Son,self).__init__(name+" . father")
# 		self.name = name
# 		# print "I AM SON :"+self.name	
# 		# super(Son,self).__work("Working")
# 		self.__work("Programing")

# 	def __work(self,name):
# 		# Father.work(self,name)
# 		print "I work in compary",name 

# 	def __del__(self):
# 		# super(Son,self).work("Working")
# 		# self.work("Working")
# 		super(Son,self).__del__()
# 		print "Son Over"

# if __name__ == '__main__':
# 	s = Son("Windard")	
# 	# super(Son,s).work("Working")

# My name is : Windard
# I word in factory Working
# My name is : Windard
# I word in factory Programing
# I work in compary Programing
# My name is : Windard
# I word in factory Working
# Father Over
# Son Over

# My name is : Windard . father
# I word in factory Working
# I work in compary Working
# My name is : Windard
# I word in factory Working
# My name is : Windard
# I word in factory Programing
# I work in compary Programing
# My name is : Windard
# I word in factory Working
# Father Over
# Son Over

# class A(object):  
#     def tell(self):  
#         print 'A tell'  
#         self.say()  
#     def say(self):  
#         print 'A say'  
#         self.__work()  
  
#     def __work(self): # private  
#         print 'A work'  
  
          
# class B(A):  
#     def tell(self):  
#         print '\tB tell'  
#         self.say()  
#         super(B,self).say()  
#         A.say(self)  
#     def say(self):  
#         print '\tB say'  
#         self.__work()  
  
#     def __work(self): # private  
#         print '\tB work'  
#         self.__run()  
  
#     def __run(self): # private  
#         print '\tB run'  
          
# b = B()  
# b.tell()  

# class A(object):  
#     def tell(self):  
#         print 'A tell'  
#         self.say()  
#     def say(self):  
#         print 'A say'  
#         self.work()  
  
#     def work(self): # public  
#         print 'A work'  
  
          
# class B(A):  
#     def tell(self):  
#         print '\tB tell'  
#         self.say()  
#         super(B,self).say()  
#         A.say(self)  
#     def say(self):  
#         print '\tB say'  
#         self.work()  
  
#     def work(self): # public  
#         print '\tB work'  
#         self.run()  
  
#     def run(self): # public  
#         print '\tB run'  
          
# b = B()  
# b.tell()  

# class FooParent(object):
#     def __init__(self):
#         self.parent='I\'m the parent.'
#         print 'Parent'
        
#     def bar(self, message):
#         print message, 'from Parent'

# class FooChild(FooParent):
#     def __init__(self):
#         FooParent.__init__(self)
#         print 'Child'
        
#     def bar(self, message):
#         FooParent.bar(self, message)
#         print 'Child bar function. '
#         print self.parent

# if __name__ == '__main__':
#     fooChild = FooChild()
#     fooChild.bar("HelloWorld")

class Father(object):

  def __init__(self,name):
      self.name = name
      # self.__firstname = name
      # self.__work("Working")
      # print "I AM FATHER :"+self.name

  # def __work(self,name):
  #     print "My name is :",self.name
  #     print "I word in factory",name

  # def __del__(self):
  #     # self.work("Working")
  #     print "Father Over"

class Son(Father):

  def __init__(self,name):
      super(Son,self).__init__(name+" . father")
      self.name = name
      print self.name
      # print super(Son,self).name
      print dir(super(Son,self))
      print super(Son,self).__dict__
      # print "I AM SON :"+self.name  
      # super(Son,self).__work("Working")
      # self.__work("Programing")

  # def __work(self,name):
  #     # Father.work(self,name)
  #     print "I work in compary",name 

  # def __del__(self):
  #     # super(Son,self).work("Working")
  #     # self.work("Working")
  #     super(Son,self).__del__()
  #     print "Son Over"

if __name__ == '__main__':
  s = Son("Windard")  
  # super(Son,s).work("Working")