from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open ("thekey.txt","wb") as file:#it will write in the thekey.txt file 
    file.write(key)

print(Fernet(key).encrypt(b"hello world"))#it will encrypt the hello world string and print it in the console