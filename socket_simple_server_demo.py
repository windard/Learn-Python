import socket
print "Creating socket..."
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "Done"

print "Connecting to remmote host...."
s.connect(('localhost',8080))
print "Done"