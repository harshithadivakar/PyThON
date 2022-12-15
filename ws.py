import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl_CERT_NONE

url = input('enter url:')
html = urllib.request.urlopen(url, 'context = ctx').read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('a')
for tag in tags :
    print(tag.get('href', None))