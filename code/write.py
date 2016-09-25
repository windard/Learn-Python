man =[]
other = []
women = []
try:
	data=open('hello.txt')
	for each in data:
		try:
			(role,line_spoken)=each.split(':')
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
	man_file = open("man_data.txt","w")
	women_file = open("women_data.txt","w")
	other_file = open("other_data.txt","w")
	# print(man,file=man_file)
	# print(women,file=women_file)
	# print(other,file=other_file)	
	man_file.write(str(man))
	women_file.write(str(women))
	other_file.write(str(other))
except IOError:
	print("File Error")
finally:	
	man_file.close()
	women_file.close()
	other_file.close()	