import requests

def response_info(r,*arg,**kwargs):
    print(r.status_code,r.url)
    print(r.text)

def response_header(r,*args,**kwargs):
    print(r.headers)


hooks = {'response':(response_info,response_header)}
r = requests.get('https://httpbin.org/get',hooks=hooks)