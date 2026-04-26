import socket

# Create a socket for the server (IPv4, TCP)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind a port to our local host
serverSocket.bind(('localhost', 8080))

# Wait until the client connects to the server
serverSocket.listen(1)
accept = serverSocket.accept()
clientConnection = accept[0]
clientAddress = accept[1]

# Get the data
data = clientConnection.recv(2048).decode()
print(data)
# Send message back
message = "Receieved input from " + str(clientAddress) + ": " + data
clientConnection.send(message.encode())

# Close the connection
clientConnection.close()
serverSocket.close()