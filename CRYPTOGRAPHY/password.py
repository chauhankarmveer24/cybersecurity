import hashlib
import os

password = b"secure_password"
salt = os.urandom(16) #genrates a 16 byte random
print(salt)

dk = hashlib.pbkdf2_hmac('sha256',password,salt,100000)
print(dk)

print("derived_key :",dk.hex())

#hashlib.sha256(password).hexdigest() => too weak for protecting real passwords
