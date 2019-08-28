'''
输出斐波那契數列前 N 个数
'''
import sys

def fab1(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b, end = ' ')
		a, b = b, a+b
		n += 1
	print()

def fab2(max):
	n, a, b = 0, 0, 1
	l = []
	while n < max:
		l.append(b)
		a, b = b, a+b
		n += 1
	return l

class fab3(object):

	def __init__(self, max):
		self._max = max
		self.n, self.a, self.b = 0, 0, 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.n < self._max:
			r = self.b
			self.a, self.b = self.b, self.a+self.b
			self.n += 1
			return r
		raise StopIteration()

def fab4(max):
	n, a, b = 0, 0, 1
	while n < max:
		#print(b, end = ' ')
		yield b
		a, b = b, a+b
		n += 1 

if __name__ == '__main__':
	count = 10

	print('\n' + '#'*15 + 'fab1' + '#'*15)
	#fab1(5)
	# <class 'NoneType'>
	print(type(fab1(count)))
	print('fab1所占空间:',sys.getsizeof(fab1(count)))

	print('\n' + '#'*15 + 'fab2' + '#'*15)
	print(fab2(count))
	# <class 'list'>
	print(type(fab2(count)))
	print('fab2所占空间:',sys.getsizeof(fab2(count)))

	print('\n' + '#'*15 + 'fab3' + '#'*15)
	print(fab3(count))
	# <class '__main__.fab3'>
	print(type(fab3(count)))
	for i in fab3(count):
		print(i, end = ' ')
	print()
	print('fab3所占空间:',sys.getsizeof(fab3(count)))

	print('\n' + '#'*15 + 'fab4' + '#'*15)
	print(fab4(count))
	# <class 'generator'>
	print(type(fab4(count)))
	for i in fab4(count):
		print(i, end = ' ')
	print()
	print('fab4所占空间:',sys.getsizeof((fab4(count))))