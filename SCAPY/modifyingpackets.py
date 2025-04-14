from scapy.all import *

packet = IP(dst="192.168.1.1",ttl=64)/TCP(dport=80,flags="S")
reply = sr1(packet,timeout=2)

if reply:
    print("Server is up and running",reply.summary())
else:
    print("Server is down")