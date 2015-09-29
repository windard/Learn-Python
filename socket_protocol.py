import socket
#[80,25,22,443,21]
def find_service_name():
	protocolname = 'tcp'
	# try:
	# except :
	# 	print "ERROR"
	for port in range(1,65535):
		try:
			print "port: %s => service name: %s" %(port,socket.getservbyport(port,protocolname))
		except:
			# print "ERROR"
			pass
	print "port: %s => service name: %s" %(53,socket.getservbyport(53,'udp'))

if __name__ == '__main__':
	find_service_name()


# port: 7 => service name: echo
# port: 9 => service name: discard
# port: 11 => service name: systat
# port: 13 => service name: daytime
# port: 17 => service name: qotd
# port: 19 => service name: chargen
# port: 20 => service name: ftp-data
# port: 21 => service name: ftp
# port: 22 => service name: ssh
# port: 23 => service name: telnet
# port: 25 => service name: smtp
# port: 37 => service name: time
# port: 42 => service name: nameserver
# port: 43 => service name: nicname
# port: 53 => service name: domain
# port: 70 => service name: gopher
# port: 79 => service name: finger
# port: 80 => service name: http
# port: 81 => service name: hosts2-ns
# port: 88 => service name: kerberos
# port: 101 => service name: hostname
# port: 102 => service name: iso-tsap
# port: 107 => service name: rtelnet
# port: 109 => service name: pop2
# port: 110 => service name: pop3
# port: 111 => service name: sunrpc
# port: 113 => service name: auth
# port: 117 => service name: uucp-path
# port: 118 => service name: sqlserv
# port: 119 => service name: nntp
# port: 135 => service name: epmap
# port: 137 => service name: netbios-ns
# port: 139 => service name: netbios-ssn
# port: 143 => service name: imap
# port: 150 => service name: sql-net
# port: 156 => service name: sqlsrv
# port: 158 => service name: pcmail-srv
# port: 170 => service name: print-srv
# port: 179 => service name: bgp
# port: 194 => service name: irc
# port: 322 => service name: rtsps
# port: 349 => service name: mftp
# port: 389 => service name: ldap
# port: 443 => service name: https
# port: 445 => service name: microsoft-ds
# port: 464 => service name: kpasswd
# port: 507 => service name: crs
# port: 512 => service name: exec
# port: 513 => service name: login
# port: 514 => service name: cmd
# port: 515 => service name: printer
# port: 520 => service name: efs
# port: 522 => service name: ulp
# port: 526 => service name: tempo
# port: 529 => service name: irc-serv
# port: 530 => service name: courier
# port: 531 => service name: conference
# port: 532 => service name: netnews
# port: 540 => service name: uucp
# port: 543 => service name: klogin
# port: 544 => service name: kshell
# port: 546 => service name: dhcpv6-client
# port: 547 => service name: dhcpv6-server
# port: 548 => service name: afpovertcp
# port: 554 => service name: rtsp
# port: 556 => service name: remotefs
# port: 563 => service name: nntps
# port: 565 => service name: whoami
# port: 568 => service name: ms-shuttle
# port: 569 => service name: ms-rome
# port: 593 => service name: http-rpc-epmap
# port: 612 => service name: hmmp-ind
# port: 613 => service name: hmmp-op
# port: 636 => service name: ldaps
# port: 666 => service name: doom
# port: 691 => service name: msexch-routing
# port: 749 => service name: kerberos-adm
# port: 800 => service name: mdbs_daemon
# port: 989 => service name: ftps-data
# port: 990 => service name: ftps
# port: 992 => service name: telnets
# port: 993 => service name: imaps
# port: 994 => service name: ircs
# port: 995 => service name: pop3s
# port: 1034 => service name: activesync
# port: 1109 => service name: kpop
# port: 1110 => service name: nfsd-status
# port: 1155 => service name: nfa
# port: 1270 => service name: opsmgr
# port: 1433 => service name: ms-sql-s
# port: 1434 => service name: ms-sql-m
# port: 1477 => service name: ms-sna-server
# port: 1478 => service name: ms-sna-base
# port: 1512 => service name: wins
# port: 1524 => service name: ingreslock
# port: 1607 => service name: stt
# port: 1711 => service name: pptconference
# port: 1723 => service name: pptp
# port: 1731 => service name: msiccp
# port: 1745 => service name: remote-winsock
# port: 1755 => service name: ms-streaming
# port: 1801 => service name: msmq
# port: 1863 => service name: msnp
# port: 1900 => service name: ssdp
# port: 1944 => service name: close-combat
# port: 2053 => service name: knetd
# port: 2106 => service name: mzap
# port: 2177 => service name: qwave
# port: 2234 => service name: directplay
# port: 2382 => service name: ms-olap3
# port: 2383 => service name: ms-olap4
# port: 2393 => service name: ms-olap1
# port: 2394 => service name: ms-olap2
# port: 2460 => service name: ms-theater
# port: 2504 => service name: wlbs
# port: 2525 => service name: ms-v-worlds
# port: 2701 => service name: sms-rcinfo
# port: 2702 => service name: sms-xfer
# port: 2703 => service name: sms-chat
# port: 2704 => service name: sms-remctrl
# port: 2725 => service name: msolap-ptp2
# port: 2869 => service name: icslap
# port: 3020 => service name: cifs
# port: 3074 => service name: xbox
# port: 3126 => service name: ms-dotnetster
# port: 3132 => service name: ms-rule-engine
# port: 3268 => service name: msft-gc
# port: 3269 => service name: msft-gc-ssl
# port: 3343 => service name: ms-cluster-net
# port: 3389 => service name: ms-wbt-server
# port: 3535 => service name: ms-la
# port: 3540 => service name: pnrp-port
# port: 3544 => service name: teredo
# port: 3587 => service name: p2pgroup
# port: 3702 => service name: ws-discovery
# port: 3776 => service name: dvcprov-port
# port: 3847 => service name: msfw-control
# port: 3882 => service name: msdts1
# port: 3935 => service name: sdp-portmapper
# port: 4350 => service name: net-device
# port: 4500 => service name: ipsec-msft
# port: 5355 => service name: llmnr
# port: 5357 => service name: wsd
# port: 5358 => service name: wsd
# port: 5678 => service name: rrac
# port: 5679 => service name: dccm
# port: 5720 => service name: ms-licensing
# port: 6073 => service name: directplay8
