import socket

server_ip = "0.0.0.0"
server_port = 12345

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#(uses IPv4,uses TCP for conncetion)
server_socket.bind((server_ip,server_port))#assigns an addresss to socket
server_socket.listen(10)#listens to 10 incoming client connections
print("server is listening")

client_socket, client_address =server_socket.accept()#accepts a clients connection
print("connection to :",client_address)

data=client_socket.recv(1024)
print("Recieved:",data.decode())#receive data from the client

message = input("you:")
client_socket.send(message.encode())#converts strings to bytes

client_socket.close()
server_socket.close()   