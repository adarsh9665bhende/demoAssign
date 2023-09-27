import socket

serverIP = "10.0.1.2"

dst_ip = str(input("Enter dstIP: "))
s = socket.socket()
#S = socket.socket()
print(dst_ip)
port = 12346

s.connect((dst_ip, port))
while True:
	htt = str(input('Enter the REquest: '))
	http = htt + '\r\n\r\n'
	s.send(http.encode())
    #S.send(http.encode())
	print(s.recv(1024).decode())


#print ('Client received '+s.recv(1024).decode())
