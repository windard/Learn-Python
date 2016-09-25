import os

if os.path.exists('test.txt'):
	data=open('test.txt')
	for each in data:
		if not each.find(':')==-1:
			(role,line_spoken) = each.split(':',1)
			print(role,end='')
			print(' said: ',end='')
			print(line_spoken,end='')
		else:
			print(each)
	data.close()
else:
	print("The data file is missing")