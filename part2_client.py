import socket

serverIP = "10.0.1.2"

dst_ip = str(input("Enter the dstIP: "))
s = socket.socket()
#S = socket.socket()
print(dst_ip)
port = 12346

s.connect((dst_ip, port))
while True:
	entered_request = str(input('Enter the REquest: '))
	final_request = entered_request + '\r\n\r\n'
	s.send(final_request.encode())
    
	print(s.recv(1024).decode())


#print ('Client received '+s.recv(1024).decode())
