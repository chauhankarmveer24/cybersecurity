import requests

file_path = 'example.txt'

data = {'username':'karm123','password':'12345'}
files = {'file':open(file_path,'rb')}#opens file in binary format

response = requests.post("https://httpbin.org/post",files=files,data=data)
print(response.json())