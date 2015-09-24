# try:
# 	with open('its.txt','w') as data:
# 		print("It's ...",file=data)
# except IOError as err:
# 	print("File error :" +str(err))
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
# try:
# 	man_file = open("man_data.txt","w")
# 	women_file = open("women_data.txt","w")
# 	other_file = open("other_data.txt","w")
# 	print(man,file=man_file)
# 	print(women,file=women_file)
# 	print(other,file=other_file)	
# except IOError:
# 	print("File Error")
# finally:	
# 	man_file.close()
# 	women_file.close()
# 	other_file.close()	
# try:
# 	with open('man_data.txt','w') as man_file:
# 		print(man,file=man_file)
# 		# man_file.write(man)
# 	with open('women_data.txt','w') as women_file:
# 		print(women,file=women_file)
# 		# women_file.write(women)
# 	with open('other_data.txt','w') as other_file:
# 		print(other,file=other_file)
# 		# other_file.write(other)
# except IOError as err:
# 	print('File error :'+str(err))

try:
	with open('man_data.txt','w') as man_file:
		print(man,file=man_file)
	with open('women_data.txt','w') as women_file:
		print(women,file=women_file)
	with open('other_data.txt','w') as other_file:
		print(other,file=other_file)
except IOError as err:
	print('File Error : '+str(err))