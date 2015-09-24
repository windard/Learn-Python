try:
	data=open('test.txt')
	for each in data:
		try:
			(role,line_spoken) = each.split(':',1)
			print(role,end='')
			print(' said: ',end='')
			print(line_spoken,end='')
		except ValueError:
			pass
	data.close()
except IOError:
	print("The data file is missing")