import socket
import threading

SERVER_IP = "0.0.0.0"
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)
print(f"Server listening on port {SERVER_PORT}...")

client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Receive messages from client
def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Client: {data.decode()}")
        except:
            break

# Send messages to client
def send_messages():
    while True:
        msg = input("you:")
        client_socket.sendall(msg.encode())

# Start chat threads
threading.Thread(target=receive_messages, daemon=True).start()
send_messages()