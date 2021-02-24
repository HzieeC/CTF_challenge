#coding:utf-8


import binascii
import string 
import zipfile
import base64
# def tansnum(s):
#     return int(s, 16)  转十六进制

dic = string.ascii_letters+string.digits+'+/=_,.*+-;:<>?!@#$%^&(){}'

def CrackCrc(crc):
    for i in dic :
        for j in dic:
            s=i+j
            s=bytes(s,encoding="UTF-8")
            if crc == (hex(binascii.crc32(s))):
                return s.decode()
                #return 
def getcrc32():
    l=[]
    for b in range(0,31,2):
        file = '压缩包.zip'
        f = zipfile.ZipFile(file,'r')
        GetCrc = f.getinfo('data'+str(b)+'.txt')
        crc = GetCrc.CRC
        l.append(hex(crc))
    return l
if __name__  == "__main__":
    #c = open('out.txt', 'w')
    l = getcrc32()
    flag=""
    for i in l:
       flag+=CrackCrc(i)
       print(flag)
    print(base64.b64decode(flag))
    #c.clo