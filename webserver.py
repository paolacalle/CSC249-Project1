from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# -------------
# Fill in start
# -------------
serverPort = 2003
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
  # TODO: Assign a port number
  #       Bind the socket to server address and server port
  #       Tell the socket to listen to at most 1 connection at a time

# -----------
# Fill in end
# -----------

while True:
    
    # Establish the connection
    print('Ready to serve...') 
    
    # -------------
    # Fill in start
    # -------------
    connectionSocket, addr = serverSocket.accept() # TODO: Set up a new connection from the client
    # -----------
    # Fill in end
    # -----------

    try:
        
        # -------------
        # Fill in start
        # -------------
        message = connectionSocket.recv(1024) # TODO: Receive the request message from the client
        # -----------
        # Fill in end
        # -----------
        
        # Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]

        # Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character
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

        connectionSocket.sendall('HTTP/1.1 200 OK\nContent-Type: text/html\n\n'.encode())

            # TODO: Send one HTTP header line into socket
        # -----------
        # Fill in end
        # -----------

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # -------------
        # Fill in start
        # -------------

        connectionSocket.sendall( "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n <doctype html><html><body><center><h1>&#x1f440; 404 Not Found &#x1f440;!!!<h1><center></body></html" .encode())
            # TODO: Send response message for file not found
            #       Close client socket
        connectionSocket.close()
        # -----------
        # Fill in end
        # -----------
#http://131.229.40.220:2003/HelloWorld.html
serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data