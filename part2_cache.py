import socket

#WRITE CODE HERE:
#1. Create a KEY-VALUE pairs (Create a dictionary OR Maintain a text file for KEY-VALUES).


dst1_ip = str(input('Enter dstTP: '))
s = socket.socket()
print ("Socket successfully created")
dport1 = 12346
s.bind((dst1_ip, dport1))
print ("socket binded to %s" %(dport1))
s.listen(5)
print ("socket is listening")
c, addr = s.accept()
print ('Got connection from', addr)

#print('Server received '+rcmsg)
#C.send('Hello client'.encode())

serverIP = "10.0.1.3"

dst_ip = str(input("Enter dstIP: "))
S = socket.socket()
print(dst_ip)
port = 12345
S.connect((dst_ip, port))

strget = "GET /assignment1?request="
http11 = " HTTP/1.1"
strok = 'HTTP/1.1 200 OK\n\n'
last = "\r\n\r\n"

map = {}
x = 0
keylist = []

rcmsg = c.recv(1024).decode()

while rcmsg:
	if rcmsg[:len(strget)] == strget and rcmsg[-len(http11 + last):] == http11 + last:
		sstring = rcmsg[len(strget):-len(http11 + last)]
		if sstring in map:                  #key
			a = strok + map[sstring] + last
			c.send(a.encode())
		else:
			S.send(sstring.encode())
			a = S.recv(1024).decode()
			if x<3:
				x += 1
			else:
				b = keylist.pop(0)
				del map[b]
			map[sstring] = a
			keylist.append(sstring)
			b = strok + a + last
			c.send(b.encode())
	else:
		a = '400 Bad Request\r\n\r\n'
		c.send(a.encode())

	rcmsg = c.recv(1024).decode()

