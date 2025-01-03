from socket import *
serverName, serverPort = "127.0.0.1", 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print("Server ready to receive")
while True:
    conn, addr = serverSocket.accept()
    print(f"Connected to {addr}")
    try:
        filename = conn.recv(1024).decode()
        with open(filename, "r") as file:
            conn.send(file.read(1024).encode())
            print(f"Sent contents of {filename}")
    except FileNotFoundError:
        conn.send("Error: File not found.".encode())
    conn.close()
