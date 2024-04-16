#import socket module
from socket import *
import sys # In order to terminate the program

def Errormessage(clientSocket):
    error = 'HTTP/1.1 404 Not Found'
    clientSocket.send(error.encode())
    clientSocket.close()

#Prepare a sever socket
serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = #Fill in start #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        clientSocket.print('HTTP/1.1 404 Not Found')
        clientSocket.close()


serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data