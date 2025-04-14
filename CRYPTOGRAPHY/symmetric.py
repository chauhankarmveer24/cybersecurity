from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
cipher = Fernet(key) #use this object to both encrypt and decrypt
print(type(cipher))
message = b"secret message"

encrypted = cipher.encrypt(message)
print(encrypted)

decrypted = cipher.decrypt(encrypted)
print(decrypted)