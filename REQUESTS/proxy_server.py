import requests

proxies = {'https':'198.211.101.99:3128'}

r = requests.get('https://httpbin.org/ip',hooks=proxies)
print(r.text)