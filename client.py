import http.client
#import time
import socket

serverIP = "10.0.1.2"

dst_ip = str(input("Enter dstIP: "))
s = socket.socket()

print(dst_ip)

port = 12346

#here establishihed connection between destnination_ip and port
s.connect((dst_ip, port))

print("Successfully established Connection")  

while True:
 try:
     inputrequest = input("Entre the request:")
     request = inputrequest

     if inputrequest=="quit" :
      print("Ending Program:")
      s.send('Ending Program'.encode())
      s.close()
 
    # spliting request by space
     inputrequest = inputrequest.split(" ")  
    
    #for valid request the length of splited must be 3

     split_lenght = len(inputrequest)

     if split_lenght != 3 :
      print("Invalid request: we will consider upto length 3")
      continue

     if inputrequest[0] == "GET" :
      inputrequest_middle = inputrequest[1]

      request = "GET /assignment2/key/val HTTP/1.1\'r\n\r\n".formay(key = inputrequest_middle)
    
    #s.send(request.encode())
    #print("Received:" + s.recv(1024).decode())

     elif inputrequest[0] =="PUT" :
    # for put we have to further split the inputrequest[1]
      inputrequest_middle =inputrequest_middle.split("/")
    #if inputrequest_middle[1] != assignment2 invalid input
        if inputrequest_middle[1] != assignment2 :
         print("Invalid request:we will consider only key")
         continue

     request ="PUT /assignment2/key/val HTTP/1.1\r\n\r\n".format(key=inputrequest_middle[0],val =inputrequest_middle[1])
    # s.send(request.encode())
     #print("Received:" + s.recv(1024).decode())

     elif inputrequest[0] =="DELETE" :
      inputrequest_middle = inputrequest[1]
      request = "DELETE  /assignment2/key/val HTTP/1.1\r\n\r\n".format(key = inputrequest_middle)
      #s.send(request.encode())
     # print("Received:" + s.recv(1024).decode())
    
     else 
      print("INvalid Request: not contain GET,PUT, or DELETE")
      continue

   s.send(request.encode())
   print("Received:" + s.recv(1024).decode())

except socket.error as error

print("Connection_Closed",error)

s.close()
#s.close()





#Write your code here:
#1. Add code to send HTTP GET / PUT / DELETE request. The request should also include KEY.
#2. Add the code to parse the response you get from the server.
#s.send('Hello server'.encode())
#print ('Client received '+s.recv(1024).decode())
