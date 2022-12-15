import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input ('Enter:')
html = urllib.request.urlopen(url,context= ctx).read()
soup = BeautifulSoup(html,'html.parser')

import re

b = list()
c=list()
x=0
tags=soup('tr')

for tag in tags:
    tag = str(tag)
    y=re.findall('([0-9]+)',tag)
    b = b+y
for d in b:
    d= int(d)
    x = x + d
print(x)

