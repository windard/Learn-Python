import socket
import sys
import argparse

host = 'localhost'

def echo_client(port,sendMessage):
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_address = (host,port)
	print "Connecting to %s port %s" %server_address
	sock.connect(server_address)

	try:
		message = sendMessage
		print "Sending %s " %message
		sock.sendall(message)
		amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_received:
			data = sock.recv(16)
			amount_received += len(data)
			print "Received : %s" %data

	except socket.errno,e:
		print "Socket error : %s" %str(e)
	except Exception,e:
		print "Other exception : %s" %str(e)
	finally:
		print "Closing connecting to the server"
		sock.close()

if __name__ == '__main__':
 	parser = argparse.ArgumentParser(description = "Socket Server Example")
 	parser.add_argument('--port',action = "store",dest = "port",type = int,required = True)
 	parser.add_argument('--message',action = "store",dest = "sendMessage",required = True)
 	given_args = parser.parse_args()
 	port = given_args.port
 	sendMessage = given_args.sendMessage
 	echo_client(port,sendMessage) 
