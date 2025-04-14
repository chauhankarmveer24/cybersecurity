import socket

server_ip = "127.1.0.1"#listens to all the interfaces
server_port = 12345

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((server_ip,server_port))

print("UDP server is listening:",server_port)

data , client_address = server_socket.recvfrom(1024)
print(client_address)
print("data received:",data.decode())
messsage = data.decode()
print("recieved from:",client_address)

server_socket.sendto("hello UDP client".encode(),client_address)