#coding=gbk
import os
import sys
import time
import getpass

Path = r"C:\Users"
User = getpass.getuser() 
startPath = os.path.join(Path,User)
os.chdir(startPath)

def group(n, sep = ','):
    s = str(abs(n))[::-1]
    groups = []
    i = 0
    while i < len(s):
        groups.append(s[i:i+3])
        i+=3
    retval = sep.join(groups)[::-1]
    if n < 0:
        return '-%s' % retval
    else:
        return retval

while 1:
	shell =  raw_input(os.getcwd()+">")
	if shell.lower().startswith("exit"):
		sys.exit()
	elif len(shell.split(" "))==1:
		try:
			if shell == "dir":
				for i in os.listdir(os.getcwd()):
					year = time.localtime(os.path.getctime(os.path.join(os.getcwd(),i))).tm_year
					month = time.localtime(os.path.getctime(os.path.join(os.getcwd(),i))).tm_mon
					day = time.localtime(os.path.getctime(os.path.join(os.getcwd(),i))).tm_mday
					hour = time.localtime(os.path.getctime(os.path.join(os.getcwd(),i))).tm_hour
					minute = time.localtime(os.path.getctime(os.path.join(os.getcwd(),i))).tm_min
					Isdir = os.path.isdir(os.path.join(os.getcwd(),i))
					if Isdir:
						print "%02d/%02d/%02d  %02d:%02d    <DIR>          %s"%(year,month,day,hour,minute,i)
					else:
						fileSize = os.path.getsize(os.path.join(os.getcwd(),i))
						print "%02d/%02d/%02d  %02d:%02d      %12s %s"%(year,month,day,hour,minute,group(fileSize),i)
			else:
				os.chdir(shell)
				shell =  raw_input(os.getcwd()+">")
		except:
			print "Your Input Is Wrong,Please Try Again"
	elif len(shell.split(" "))==2:
		try:
			order = shell.split(" ")[0]
			content = shell.split(" ")[1]
			if order == "cd" or order == "chdir":
				newPath = os.path.join(os.getcwd(),content)
				try:
					os.chdir(newPath)
				except:
					print "系统找不到指定的路径。"
			elif order == "mkdir":
				os.mkdir(content)
				print "New Dir Was Created"
			else:
				print "Your Input Is Wrong,Please Try Again"
		except:
			print "Your Input Is Wrong,Please Try Again"
	else:
		print "Your Input Is Wrong,Please Try Again"