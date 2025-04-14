from scapy.all import *

answered , unanswered = sr(IP(dst="198.162.1.1")/ICMP(),timeout=2,verbose=False)
answered.summary()
unanswered.summary()

print("Active Hosts (Replied):")
for snd, rcv in answered:
    print(rcv.src)#prints ip address that are active

print("\nInactive Hosts (No Reply):")
for pkt in unanswered:
    print(pkt.src,pkt.dst)#ip of host that didnt reply