import socket
#import http.server

#dictionary creation
keyValueDict = dict()


#ip addresses and ports
serverIP=str(input("Enter Server IP: "))
dst_ip=serverIP
dport=12346

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket successfully created")

s.bind((dst_ip, dport))
print ("socket binded to %d" %(dport))

s.listen(5)
print ("socket is listening")

while True:
  
  try:
    c, addr = s.accept()
    print ('Got connection from: ', addr )

    while True:
      recvmsg = c.recv(1024).decode()
      print('Server received: '+ recvmsg)
      

      #if client quits the session, conncection gets disconnected
      if recvmsg == "quit":
        print('Disconnected : Client has disconnected')
        break
      
       # print('Disconnected : Client disconnected due to an interrupt')
       # break
      if recvmsg == "":
        break
      
      #traverse recieved message
      recv_request = recvmsg.split(" ")
      recv_first_part = recv_request[0]
      recv_middle_part = recv_request[1]


      #first_parttions GET , PUT , DELETE
      if recv_first_part == "GET":
        recv_key = recv_middle_part.split("=")[1]
        if recv_key in keyValueDict :
          msg = "HTTP/1.1 200 OK\r\n\r\n" + keyValueDict[recv_key]
          c.send(msg.encode())
        else:
          msg = "HTTP/1.1 404 Not Found \r\n\r\n No such key exists!"
          c.send(msg.encode())

      elif recv_first_part == "PUT":
        recv_key = recv_middle_part.split("/")[2]
        rec_val = recv_middle_part.split("/")[3]
        keyValueDict[recv_key] = rec_val
        c.send("HTTP/1.1 200 OK\r\n\r\nPush sucess!".encode())

      elif recv_first_part == "DELETE":
        recv_key = recv_middle_part.split("/")[2]
        if recv_key in keyValueDict:
          keyValueDict.pop(recv_key)
          c.send("HTTP/1.1 200 OK\r\n\r\nDelete success!".encode())
        else:
          c.send("HTTP/1.1 404 Not Found\r\n\r\nDelete failure!: Key does not exist".encode())

          
      else:
        c.send("HTTP/1.1 400 Bad Request\r\n\r\nInvalid request!: Command not found".encode())
      print("Key Val: ", keyValueDict)
      
    c.close()
  except socket.error as e:
    print("Error: ", e)
    c.close()
    break
