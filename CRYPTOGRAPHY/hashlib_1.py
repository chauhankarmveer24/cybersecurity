import hashlib

#input data
data = "Hello, World!".encode()

#SHA-256
hash_object = hashlib.sha256(data)
print(hash_object)
hex = hash_object.hexdigest()
print("SHA256 hash:",hex)
# hexx = hex.decode( ) => hash cannot be decoded