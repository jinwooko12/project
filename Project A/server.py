# import socket module
from socket import *
import sys
import threading

threads = []

#making thread to multitasking of server.
def startThread(clientSocket):
    t = threading.Thread(target=encodingTargetClient, args=(clientSocket, ), daemon=True)
    t.start()
    threads.append(t)


#assigning the target client to Thread
def encodingTargetClient(clientSocket):
    outputData = defFileName(clientSocket)
    sendHeader(clientSocket)
    for i in range(0, len(outputData)):
        clientSocket.send(outputData[i].encode())
    clientSocket.send("\r\n".encode())
    clientSocket.close()


#receive file name and encode to read outputData
def defFileName(clientSocket):
    message = clientSocket.recv(4096).decode()
    filename = message.split()[1]
    f = open(filename[1:], encoding='UTF-8')
    outputData = f.read()
    f.close()
    return outputData

#send header to read HTML file
def sendHeader(clientSocket):
    header = 'HTTP/1.1 200 OK\n'
    contentType= 'content-type: text/html\n'
    clientSocket.send(header.encode())
    clientSocket.send(contentType.encode())
    clientSocket.send('\r\n\r\n'.encode())

#send error msg
def sendErr(clientSocket):
    error = 'HTTP/1.1 404 Not Found\n'
    clientSocket.send(error.encode())
    clientSocket.close()


# Prepare a sever socket
serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    clientSocket, addr = serverSocket.accept()
    print('connected by', addr)
    try:
        print('Thread', len(threads)+1, 'is Excuting...')
        startThread(clientSocket)
    except IOError:
        sendErr(clientSocket)


serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data