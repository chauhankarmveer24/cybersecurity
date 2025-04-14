from scapy.all import sniff, wrpcap, rdpcap

packets = sniff(count=10)
wrpcap("captured.pcap",packets)
packets.summary()

#to read the pcap files
pcap = rdpcap("captured.pcap")
for pkt in pcap:
    print(pkt.summary())