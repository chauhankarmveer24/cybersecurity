#!/usr/bin/env python3
from cryptography.fernet import Fernet
import os
import argparse
from colorama import init, Fore

# Initialize colorama
init()

def generate_key():
    """Generate a new encryption key."""
    return Fernet.generate_key()

def save_key(key, key_file):
    """Save the encryption key to a file."""
    with open(key_file, 'wb') as f:
        f.write(key)

def load_key(key_file):
    """Load the encryption key from a file."""
    with open(key_file, 'rb') as f:
        return f.read()

def encrypt_file(file_path, key):
    """Encrypt a file using the provided key."""
    try:
        # Read the file content
        with open(file_path, 'rb') as f:
            data = f.read()
        
        # Encrypt the data
        f = Fernet(key)
        encrypted_data = f.encrypt(data)
        
        # Write the encrypted data back to the file
        with open(file_path + '.encrypted', 'wb') as f:
            f.write(encrypted_data)
        
        print(f"{Fore.GREEN}[+] File encrypted successfully: {file_path}.encrypted{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error encrypting file: {str(e)}{Fore.RESET}")

def decrypt_file(file_path, key):
    """Decrypt a file using the provided key."""
    try:
        # Read the encrypted file
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        
        # Decrypt the data
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data)
        
        # Write the decrypted data to a new file
        decrypted_file = file_path.replace('.encrypted', '.decrypted')
        with open(decrypted_file, 'wb') as f:
            f.write(decrypted_data)
        
        print(f"{Fore.GREEN}[+] File decrypted successfully: {decrypted_file}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error decrypting file: {str(e)}{Fore.RESET}")

def main():
    parser = argparse.ArgumentParser(description='File Encryption Tool')
    parser.add_argument('--generate-key', action='store_true', help='Generate a new encryption key')
    parser.add_argument('--key-file', default='encryption.key', help='Path to the key file')
    parser.add_argument('--encrypt', help='Path to the file to encrypt')
    parser.add_argument('--decrypt', help='Path to the file to decrypt')
    
    args = parser.parse_args()
    
    if args.generate_key:
        key = generate_key()
        save_key(key, args.key_file)
        print(f"{Fore.GREEN}[+] New encryption key generated and saved to {args.key_file}{Fore.RESET}")
        return
    
    if not os.path.exists(args.key_file):
        print(f"{Fore.RED}[!] Key file not found. Generate a new key using --generate-key{Fore.RESET}")
        return
    
    key = load_key(args.key_file)
    
    if args.encrypt:
        if not os.path.exists(args.encrypt):
            print(f"{Fore.RED}[!] File to encrypt not found: {args.encrypt}{Fore.RESET}")
            return
        encrypt_file(args.encrypt, key)
    
    if args.decrypt:
        if not os.path.exists(args.decrypt):
            print(f"{Fore.RED}[!] File to decrypt not found: {args.decrypt}{Fore.RESET}")
            return
        decrypt_file(args.decrypt, key)

if __name__ == "__main__":
    main() 