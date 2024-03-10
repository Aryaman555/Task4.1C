import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

client_socket.connect((host, port))

client_socket.send("Hello".encode())

server_response = client_socket.recv(1024).decode()
print("Received from server:", server_response)

name = input("Enter your name: ")

client_socket.send(name.encode())

welcome_message = client_socket.recv(1024).decode()
print("Received from server:", welcome_message)

client_socket.close()
