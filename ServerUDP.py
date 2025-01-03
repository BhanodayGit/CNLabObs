from socket import *
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", 12000))
print("Server ready to receive")

while True:
    filename, clientAddress = serverSocket.recvfrom(2048)
    try:
        with open(filename.decode(), "r") as file:
            serverSocket.sendto(file.read(2048).encode(), clientAddress)
    except FileNotFoundError:
        serverSocket.sendto("File not found".encode(), clientAddress)
