import requests

headers = {'content-type':'multipart/form-data'}
r = requests.post("https://httpbin.org/post",headers=headers)

print(r.request)