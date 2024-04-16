from socket import *
import threading
import sys

def client_thread(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        with open(filename[1:], 'rb') as f:
            outputdata = f.read()
            connectionSocket.send(b"HTTP/1.1 200 OK\r\n")
            connectionSocket.send(b"Content-Type: text/html\r\n")
            connectionSocket.send(b"\r\n")
            connectionSocket.send(outputdata)
    except IOError:
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n")
        connectionSocket.send(b"Content-Type: text/html\r\n")
        connectionSocket.send(b"\r\n")
        connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>")
    finally:
        connectionSocket.close()

def start_server(serverPort):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    print(f"Server is ready to receive on port {serverPort}")

    while True:
        connectionSocket, addr = serverSocket.accept()
        threading.Thread(target=client_thread, args=(connectionSocket,)).start()

    serverSocket.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py server_port")
    else:
        serverPort = int(sys.argv[1])
        start_server(serverPort)
