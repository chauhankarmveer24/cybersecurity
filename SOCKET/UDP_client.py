import socket

server_ip = "127.1.0.1"
server_port = 12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 
message = "Hello , UDP server"

client_socket.sendto(message.encode(),(server_ip,server_port))

response , server_address = client_socket.recvfrom(1024)
print("received from the server:",response.decode())