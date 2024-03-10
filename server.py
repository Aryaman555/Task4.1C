import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

server_socket.bind((host, port))

server_socket.listen(5)

print("Server listening on {}:{}".format(host, port))

while True:
    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)

    message = client_socket.recv(1024).decode()
    print("Received from client:", message)

    client_socket.send("Hello, What's your name?".encode())

    name = client_socket.recv(1024).decode()
    print("Received name from client:", name)

    welcome_message = "Hello {}, Welcome to SIT202".format(name)
    client_socket.send(welcome_message.encode())

    client_socket.close()
