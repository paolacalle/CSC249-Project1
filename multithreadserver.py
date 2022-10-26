import threading
from socket import *

from socket import *
import sys  # In order to terminate the program

class RequestedThread(threading.Thread):
    # print("HELLO")
    def __init__(self, clientSocket, clientAddress):
        threading.Thread.__init__(self)
        print(clientSocket)
        self.connectionSocket = clientSocket
        self.addr = clientAddress
        print("New connection has been added:", clientAddress)

    def run(self):
        print("Connection found!")
        while True:
            print("True")
            try:
                print("Trying")
                message = self.connectionSocket.recv(1024)  # TODO: Receive the request message from the client
                # print(message)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()  # TODO: Store the entire contents of the requested file in a temporary buffer

                self.connectionSocket.sendall('HTTP/1.1 200 OK\nContent-Type: text/html\n\n'.encode())

                for i in range(0, len(outputdata)):
                    self.connectionSocket.send(outputdata[i].encode())
                self.connectionSocket.send("\r\n".encode())
                self.connectionSocket.close()

                break
            except IOError:
                print("IOError")
                self.connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
                self.connectionSocket.send("<html><head></head><body><h1>404 Not Found &#x1f440;</h1></body></html>\r\n".encode())
                self.connectionSocket.close()

                break

if __name__ == "__main__":
    threads = []
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverPort = 2003

    serverSocket.bind(('', serverPort))

    while True:
        serverSocket.listen(1)
        print('Mutithreading is ready to serve...')

        connectionSocket, addr = serverSocket.accept()  # TODO: Set up a new connection from the client
        print(f"-----{connectionSocket}----")
        newThread = RequestedThread(connectionSocket, addr)
        threads.append(newThread)
        newThread.start()
        newThread.join()
    #http://131.229.40.220:2003/HelloWorld.html
    serverSocket.close()
    print(threads)
sys.exit()  # Terminate the program after sending the corresponding data
