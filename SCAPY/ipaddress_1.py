import socket

website = "google.com"
ip_address = socket.gethostbyname(website)

print(f"The IP address of {website} is {ip_address}")
