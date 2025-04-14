import requests

url = "https://httpbin.org/cookies"
cookies = {'location':'new york'}

r = requests.get(url,cookies=cookies)

requestjar = requests.cookies.RequestsCookieJar()
print(requestjar)
requestjar.set("username","karm123",domain="httpbin.org",path="/cookies")
requestjar.set("Cartitem","laptop",domain="httpbin.org",path="/cookies")

r3 = requests.get(url,cookies=requestjar)
print(r3.text)