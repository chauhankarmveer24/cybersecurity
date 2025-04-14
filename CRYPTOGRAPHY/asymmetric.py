from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048) #given to individual user , used for decryption
print(private_key)

public_key = private_key.public_key() #given to server, generated from pvt key and is used for encryption
print(public_key)

message = b"hello"

cipher_text = public_key.encrypt(message,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
print(f"encrypted: {cipher_text}")

plain_text = private_key.decrypt(cipher_text,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
print(f"decrypted: {plain_text}")