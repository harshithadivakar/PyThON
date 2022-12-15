import urllib.request , urllib.parse , urllib.error 
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url  = input('Enter url:')
html = urllib.request.urlopen(url, context = None).read()

hello = json.loads(html)
dello = hello['comments']
x= list()
for d in dello :
	x.append(d['count'])
print(sum(x))