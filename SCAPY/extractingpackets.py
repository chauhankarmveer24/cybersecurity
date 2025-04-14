from scapy.all import *

packet = IP(dst="198.162.1.1")
print(packet.dst)
print(packet.ttl)