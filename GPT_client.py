from socket import *
import sys

def http_client(server_host, server_port, filename):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((server_host, server_port))
    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    clientSocket.send(request.encode())
    
    response = clientSocket.recv(4096)
    print(response.decode())
    clientSocket.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python client.py server_host server_port filename")
    else:
        server_host = sys.argv[1]
        server_port = int(sys.argv[2])
        filename = sys.argv[3]
        http_client(server_host, server_port, filename)
