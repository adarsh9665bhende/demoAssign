#new file
# import http.client
#import time
import socket

serverIP = "10.0.1.2"

dst_ip = str(input("Enter dstIP: "))
#s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(dst_ip)

dport = 12346

# here establish connection between destination_ip and port



s.connect((dst_ip, dport))

print("Successfully established Connection")  

while True:
    try:
        inputrequest = input("Enter the request:")
        request = inputrequest

        if inputrequest == "quit": 
            print("Ending Program:")
            s.send('Ending Program'.encode())
            s.close()
            break;
 
        # splitting request by space
        inputrequest = inputrequest.split(" ")  
    
        # for valid request, the length of split must be 3
        split_length = len(inputrequest)

        if split_length != 3 :
            print("Invalid request: we will consider up to length 3")
            continue

        if inputrequest[0] == "GET":
            inputrequest_middle = inputrequest[1]
            inputrequest_middle = inputrequest_middle.split("=")
            if len(inputrequest_middle)!=2:
               print("INvalid Input:length of middle p[art ius not 2]")
            else :
               request = "GET /assignment2/key/val HTTP/1.1\r\n\r\n".format(key = inputrequest_middle)


           
    
        #s.send(request.encode())
        #print("Received:" + s.recv(1024).decode())

        elif inputrequest[0] =="PUT":
            # for put, we have to further split the inputrequest[1]
            inputrequest_middle = inputrequest[1].split("=")
            # if inputrequest_middle[1] != assignment2, invalid input
            if inputrequest_middle[1] != "assignment2":
                print("Invalid request: we will consider only key")
                continue


            request = "PUT /assignment2/{key}/{val} HTTP/1.1\r\n\r\n".format(key = inputrequest_middle[2],val = inputrequest_middle[1])
            print(request)
            # request =f"PUT /assignment2/{inputrequest_middle[0]}/{inputrequest_middle[1]} HTTP/1.1\r\n\r\n"
            # request = "PUT /assignment2/"
            # request = request + inputrequest_middle[0]
            # request = request + "/"
            # request = request + inputrequest_middle[1]
            # request =

        elif inputrequest[0] =="DELETE":
            inputrequest_middle = inputrequest[1]
            request = "DELETE  /assignment2/key/val HTTP/1.1\r\n\r\n".format(key = inputrequest_middle)
            #s.send(request.encode())
            # print("Received:" + s.recv(1024).decode())
    
        else:
            print("Invalid Request: does not contain GET, PUT, or DELETE")
            continue

        s.send(request.encode())
        print("Received:" + s.recv(1024).decode())

    except socket.error as error:
        print("Connection Closed", error)

s.close()
#s.close()
