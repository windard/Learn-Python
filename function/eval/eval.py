std_1, std_2, std_3, std_4 = ['test1'], ['test2'], ['test3'], ['test4']

print('#######\teval function\t#######')
for i in range(1, 5):
	print(eval('std_'+str(i)))

print('#######\texec function\t#######')
for i in range(1, 5):
	print(exec('std_'+str(i)))

print('#######\tdict function\t#######')
dict = {}
dict['std_1'] = std_1
dict['std_2'] = std_2
dict['std_3'] = std_3
dict['std_4'] = std_4
for i in range(1, 5):
	print(dict['std_'+str(i)])

# https://stackoverflow.com/questions/11553721/using-a-string-variable-as-a-variable-name
# https://stackoverflow.com/questions/2259224/python-inserting-a-variable-value-into-a-variable-name