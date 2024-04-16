from socket import *


serverHost = gethostname()
serverPort = int(input('input port#: '))
fileName = input('input FileName: ')

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))

getFile = 'GET /'+ fileName + ' HTTP/1.1'
clientSocket.send(getFile.encode())
clientSocket.send('\r\n'.encode())

message = clientSocket.recv(4096)
print('From Server:', message.decode())

clientSocket.close()





