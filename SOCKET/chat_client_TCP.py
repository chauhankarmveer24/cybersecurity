import socket
import threading

SERVER_IP = "127.0.0.1"  # Or LAN IP of the server
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
print("Connected to server.")

# Receive messages from server
def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Server: {data.decode()}")
        except:
            break

# Send messages to server
def send_messages():
    while True:
        msg = input()
        client_socket.sendall(msg.encode())

# Start chat threads
threading.Thread(target=receive_messages, daemon=True).start()
send_messages()
