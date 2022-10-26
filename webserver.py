from socket import *
import sys
# We are creating a TCP server socket
# AF_INT is used for IPv4 protocols
# SOCK_STREAM is used for TCP

serverSocket = socket(AF_INET, SOCK_STREAM)

# # getting the hostname by socket.gethostname() method
# hostname = gethostname()
#
# # getting the IP address using socket.gethostbyname() method
# ip_address = gethostbyname(hostname)
#
# # printing the hostname and ip_address
# print("Getting local address...")
# print(f"Hostname: {hostname}")
# print(f"IP Address: {ip_address}")

# -------------
# Fill in start
# -------------
serverPort = 2003
serverSocket.bind(('', serverPort)) #Binds socket to address
serverSocket.listen(1) #listens to at most 1 connection at a time

  # TODO: Assign a port number
  #       Bind the socket to server address and server port
  #       Tell the socket to listen to at most 1 connection at a time

# -----------
# Fill in end
# -----------

#The server should now be running and listening for incoming connections
while True:

    print('Ready to serve...')
    
    # -------------
    # Fill in start
    # -------------
    clientSocket, addr = serverSocket.accept() # TODO: Set up a new connection from the client
    # print(f"Connection established from address {addr}")
    # -----------
    # Fill in end
    # -----------

    #If an exception occurs in try block, the rest of the code is skipped.
    try:
        
        # -------------
        # Fill in start
        # -------------
        message = clientSocket.recv(1024) # TODO: Receive the request message from the client
        # -----------
        # Fill in end
        # -----------
        
        # Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]

        # Because the extracted path of the HTTP request includes 
		# a character '/', we read the path from the second character; to open our file we just add it after the /
        f = open(filename[1:])
        
        # -------------
        # Fill in start
        # -------------
        outputdata = f.read() #recv_into(1024) # TODO: Store the entire contents of the requested file in a temporary buffer
        # -----------
        # Fill in end
        # -----------

        # -------------
        # Fill in start
        # -------------

        clientSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

            # TODO: Send one HTTP header line into socket
        # -----------
        # Fill in end
        # -----------

        # Send the content of the requested file to the client
        # Starts from 0 up to the length of outputdata
        for i in range(0, len(outputdata)):
            clientSocket.send(outputdata[i].encode()) #sends each item indvidually
        clientSocket.send("\r\n".encode())

        clientSocket.close()

        break

    except IOError:
        # -------------
        # Fill in start
        # -------------
        # TODO: Send response message for file not found

        clientSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        clientSocket.send("<html><head></head><body><h1>404 Not Found &#x1f440;</h1></body></html>\r\n")
        clientSocket.close() #Close client socket

        break
        # -----------
        # Fill in end
        # -----------
#http://131.229.40.220:2003/HelloWorld.html
serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data