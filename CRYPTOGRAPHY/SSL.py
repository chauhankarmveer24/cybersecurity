import ssl
import socket

host = "www.google.com" #server you are trying to connect
port = 443

context = ssl.create_default_context()#creates secure ssl / tls
print("context:",context)

sock = socket.create_connection((host,port)) #creates a socket connection
print("sock:",sock)

ssock = context.wrap_socket(sock,server_hostname=host) #wraps the socket in a SSl / TLS socket
print("ssock:",ssock)

print(ssock.getpeercert()) #certificate is a digital identity card for the server