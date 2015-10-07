import socket

host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind((host,port))
print "waiting for connecting..."
s.listen(5)

while 1:
	clientsock,clientaddr = s.accept()
	print "Got connecting from",clientsock.getpeername()
	clientsock.close()