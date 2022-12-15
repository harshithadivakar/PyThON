import urllib.request , urllib.parse , urllib.error
import xml.etree.ElementTree as ET

url = input ('Enter')
html = urllib.request.urlopen(url , context = None).read()
tree = ET.fromstring(html)
hello = tree.findall('comments/comment')
y=list()
for h in hello:
	y.append(int(h.find('count').text))
print(sum(y))