'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile
import sys
# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False


def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for line in f:
                password = line.strip()
                if attempt_extract(zf,password):
                    print("[+] Password found:", password.decode())
                    return
    print("[+] Password not found in list")

if __name__ == "__main__":
    main()