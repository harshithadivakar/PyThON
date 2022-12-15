fname=input("enter file name:")
handle = open(fname)
a = list()
b = list()
c=0
import re
for lines in handle:
    a = re.findall('[0-9]+' , lines)
    b=b+a
for x in b:
    x = int(x)
    c = c+x
print(c)