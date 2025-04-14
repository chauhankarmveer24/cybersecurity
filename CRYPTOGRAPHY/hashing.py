from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA256())
print(digest)
digest.update(b"hello")
print(digest)

hash_value = digest.finalize()
print(hash_value.hex())