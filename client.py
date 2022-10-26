from socket import *
import sys

server_host = sys.argv[1]
server_port = sys.argv[2]
filename = sys.argv[3]

# print(server_host, server_port, filename)

s = socket(AF_INET, SOCK_STREAM)

s.connect((server_host, int(server_port)))

HTTPMessage = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}:{server_port}\r\nConnection: keep-alive\r\n"

bytes = str.encode(HTTPMessage)

s.sendall(bytes)

# Recving the data
allRevieved = []
while (True):

    inputdata = s.recv(1024)

    allRevieved.append(inputdata)

    if (inputdata == b''):
        print("Data Recvied:\n", allRevieved)
        print("Connection closed")

        break

s.close()
sys.exit()


