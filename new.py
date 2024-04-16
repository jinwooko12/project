# Import socket module
from socket import *
import sys  # In order to terminate the program

# Prepare a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Fill in start
# Assign a port number
serverPort = 6789  # Replace with your port number
# Bind the socket to server address and server port
serverSocket.bind(('', serverPort))
# Tell the socket to listen for incoming connections
# Listen to at most 1 connection at a time
serverSocket.listen(1)
# Fill in end

print('The server is ready to receive')

while True:
    # Establish the connection
    print('Ready to serve...')
    # Fill in start
    # Accept a new connection from the client
    connectionSocket, addr = serverSocket.accept()
    # Fill in end

    try:
        # Fill in start
        # Receive the HTTP request from the client
        message = connectionSocket.recv(1024).decode()
        # Fill in end

        filename = message.split()[1]
        # Open the requested file and read it
        f = open(filename[1:])
        # Fill in start
        # Read the file "f" and store its contents
        outputdata = f.read()
        f.close()
        # Fill in end

        # Send one HTTP header line into socket
        # Fill in start
        # HTTP header lines
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        connectionSocket.send('Content-Type: text/html\r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        connectionSocket.send('Content-Type: text/html\r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>'.encode())
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

# Close server socket and terminate program (this part is never reached due to the loop)
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
