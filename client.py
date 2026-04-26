import socket

# Create a socket object for the client
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
clientSocket.connect(('localhost', 8080))

# Send a message to the server
clientMessage = "Hello server, please write back!"
clientSocket.send(clientMessage.encode())

serverResponse = clientSocket.recv(2048).decode()
print("Server's response: " + serverResponse)

clientSocket.close()