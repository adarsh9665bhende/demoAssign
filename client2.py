import socket

serverIP = "10.0.1.2"
port = 12346

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    dst_ip = input("Enter dstIP: ")
    print(dst_ip)

    s.connect((dst_ip, port))
    print("Successfully established Connection")

    while True:
        try:
            inputrequest = input("Enter the request: ")
            request = inputrequest

            if inputrequest == "quit":
                print("Ending Program:")
                s.send('Ending Program'.encode())
                s.close()
                break

            inputrequest = inputrequest.split(" ")

            if len(inputrequest) != 3:
                print("Invalid request: we will consider up to length 3")
                continue

            if inputrequest[0] == "GET":
                inputrequest_middle = inputrequest[1]

                request = f"GET /assignment2/{inputrequest_middle} HTTP/1.1\r\n\r\n"

            elif inputrequest[0] == "PUT":
                inputrequest_middle = inputrequest[1].split("/")
                if len(inputrequest_middle) != 3:
                    print("Invalid request: we will consider only key")
                    continue

                request = f"PUT /assignment2/{inputrequest_middle[0]}/{inputrequest_middle[1]} HTTP/1.1\r\n\r\n"

            elif inputrequest[0] == "DELETE":
                inputrequest_middle = inputrequest[1]

                request = f"DELETE /assignment2/{inputrequest_middle} HTTP/1.1\r\n\r\n"

            else:
                print("Invalid Request: does not contain GET, PUT, or DELETE")
                continue

            s.send(request.encode())
            print("Received: " + s.recv(1024).decode())

        except socket.error as error:
            print("Connection Closed", error)

except socket.error as error:
    print("Connection Closed", error)

s.close()
