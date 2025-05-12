import subprocess
import platform
import socket
import sys

def ping(host):
    """
    Returns True if host responds to a ping request
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def check_network():
    print("\nNetwork Diagnostic Tool")
    print("=" * 50)
    
    # Check localhost
    print("\n1. Checking localhost...")
    if ping("127.0.0.1"):
        print("✓ Localhost is responding")
    else:
        print("✗ Localhost is not responding - Check your network stack")
    
    # Check default gateway
    print("\n2. Checking default gateway...")
    gateway = "192.168.145.254"  # Your gateway from ipconfig
    if ping(gateway):
        print(f"✓ Gateway {gateway} is responding")
    else:
        print(f"✗ Gateway {gateway} is not responding - Check your router")
    
    # Check DNS
    print("\n3. Checking DNS resolution...")
    try:
        socket.gethostbyname('google.com')
        print("✓ DNS resolution is working")
    except socket.gaierror:
        print("✗ DNS resolution failed - Check your DNS settings")
    
    # Check internet connectivity
    print("\n4. Checking internet connectivity...")
    if ping("8.8.8.8"):
        print("✓ Internet is accessible")
    else:
        print("✗ No internet connectivity - Check your ISP connection")

if __name__ == "__main__":
    check_network() 