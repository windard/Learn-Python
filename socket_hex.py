import socket
from binascii  import hexlify

def convert_ip4_adderss():
	for ip in ['127.0.0.1','192.168.0.1']:
		# print ip
		packed_ip_address = socket.inet_aton(ip)
		unpacked_ip_address = socket.inet_ntoa(packed_ip_address)
		print "ip adress :"+unpacked_ip_address+"Packed adress :"+hexlify(packed_ip_address) 

if __name__ == '__main__':
	convert_ip4_adderss()