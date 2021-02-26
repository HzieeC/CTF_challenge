import urllib.parse
import re
sql=[]
for i in range(326):
    f=open("./file/select7({}).php".format(str(i+1)))
    sql.append(f.read())
    f.close()

for i in sql:
    if re.findall(r"!=(.*?),",urllib.parse.unquote(i)):
        flag=re.findall(r"!=(.*?),",urllib.parse.unquote(i))[0]
        print(chr(int(flag)),end="")