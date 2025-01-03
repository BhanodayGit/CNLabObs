from socket import *
serverName, serverPort = "127.0.0.1", 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
filename = input("Enter file name: ")
clientSocket.sendto(filename.encode(), (serverName, serverPort))
data, _ = clientSocket.recvfrom(2048)
print("From Server:", data.decode())
clientSocket.close()
