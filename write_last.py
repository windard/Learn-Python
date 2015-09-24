import sys

def print_lol(the_list,indent=False,level=0,fn=sys.stdout):
	for each in the_list:
		if isinstance(each,list):
			print_lol(each,indent,level+1,fn)
		else:
			if indent:
				for tab in range(level):
					print("\t",end='',file=fn)
				print(each,file=fn)
			else:
				print(each,file=fn)

man =[]
other = []
women = []
try:
	data=open('hello.txt')
	for each in data:
		try:
			(role,line_spoken)=each.split(':',1)
			line_spoken = line_spoken.strip()
			if role=='Man':
				man.append(line_spoken)
			elif role=='Other':
				other.append(line_spoken)
			elif role=='Women':
				women.append(line_spoken)
			else:
				pass
		except ValueError:
			pass
	data.close()		
except IOError:
	print("The data file is missing")

try:
	with open('man_data.txt','w') as man_file:
		print_lol(man,fn=man_file)
	with open('women_data.txt','w') as women_file:
		print_lol(women,fn=women_file)
	with open('other_data.txt','w') as other_file:
		print_lol(other,fn=other_file)
except IOError as err:
	print('File Error : '+str(err))