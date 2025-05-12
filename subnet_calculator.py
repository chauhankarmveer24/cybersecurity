import ipaddress
import sys

def calculate_subnet(ip, subnet_mask):
    try:
        # Create network object
        network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)
        
        print("\nSubnet Information:")
        print(f"Network Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Total IP Addresses: {network.num_addresses}")
        print(f"Usable IP Addresses: {network.num_addresses - 2}")
        print(f"First Usable IP: {network.network_address + 1}")
        print(f"Last Usable IP: {network.broadcast_address - 1}")
        
    except ValueError as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python subnet_calculator.py <IP> <subnet_mask>")
        print("Example: python subnet_calculator.py 192.168.1.1 255.255.255.0")
        return
    
    ip = sys.argv[1]
    subnet_mask = sys.argv[2]
    calculate_subnet(ip, subnet_mask)

if __name__ == "__main__":
    main() 