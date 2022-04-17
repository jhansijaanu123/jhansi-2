import re
ip1="jaanu"
ip2="jhansi"
c=0
for i in ip1:
    if re.search(i,ip2):
        c=c+1
print("no. of matching characters are",c)        