import requests

headers = {'Authorization':'Bearer karm1234'}
response = requests.get("https://httpbin.org/get",params=headers)
#get req : params , post req : data
#print(response.text)
print(response.url)
print(response.status_code)