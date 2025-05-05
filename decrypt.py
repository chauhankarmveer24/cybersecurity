import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file.endswith(".py") or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

print("[+] Files to decrypt:", files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

cipher = Fernet(secretkey)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = cipher.decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

print("[+] Decryption complete.")
