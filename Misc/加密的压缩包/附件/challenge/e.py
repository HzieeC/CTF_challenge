import base64
flag="xgctf{**************}"
flag_base64=base64.b64encode(flag.encode())
print(flag_base64)
for i in range(0,len(flag_base64),2):
    f=open("data{}.txt".format(str(i)),"wb")
    f.write(flag_base64[i:i+2])
    f.close()