from scapy.all import *

packet = IP(dst="198.162.1.1")/ICMP()
send(packet)
print(packet.summary())