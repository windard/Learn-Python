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

movie=['the Meaning Of life',1987,'the Holy of Love',['Monkey King Is Coming',2015,['Love You Forever',2010,'Hello World',1990]]]
print_lol(movie)