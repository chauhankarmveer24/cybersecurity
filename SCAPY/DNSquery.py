from scapy.all import *

packet = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="yahoo.com"))
response = sr1(packet)
print(response.show())