from scapy.all import *

def packet_callback(packet):
    print(packet.summary())  # Prints summary of the packet

# Captures 10 packets from the "Wi-Fi" interface
sniff(prn=packet_callback, count=10, iface="Wi-Fi")