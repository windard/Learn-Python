import socket

def get_remote_info():
	remote_host = "www.python.org"
	try:
		print "IP Address " + socket.gethostbyname(remote_host)
	except socket.error,err_msg:
		print remote_host,err_msg

if __name__ == '__main__':
	get_remote_info()