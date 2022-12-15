import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter the link:')
html = urllib.request.urlopen(url, context= ctx).read()
soup = BeautifulSoup( html )
line = input('Enter the line number')
line = int(line)-1
count = input('Enter count:')
count=  int(count) 

for i in range(count):
    soup = BeautifulSoup( html , 'html.parser')
    tags = soup('a')
    html = urllib.request.urlopen(tags[line].get('href', None)).read()
    print(tags[line].contents[0])  