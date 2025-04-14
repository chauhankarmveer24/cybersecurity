import socket

server_ip = "127.1.0.1"
server_port = 12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((server_ip,server_port))
print("connected to the server")

message = input("you:")
client_socket.send(message.encode())#strings into bytes
data = client_socket.recv(1024)
print("Recieved data from server:",data.decode())#bytes into strings

client_socket.close()