from socket import *

ServerHost = gethostname()
ServerPort = int(input('port number: '))
fileName = input('File Name: ')
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((ServerHost, ServerPort))

getfile = 'get /' + fileName + 'HTTP/ 1.1'
clientSocket.send(getfile.encode())
clientSocket.send('\r\n'.encode())

message = clientSocket.recv(1024)
print('From Server:', message.decode())
clientSocket.close()
