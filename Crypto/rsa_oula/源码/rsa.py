from Crypto.Util.number import *
from flag import FLAG
import random

msg = FLAG
hex_msg=int.from_bytes(msg.encode(),'big')

def rsaEncode():
    f=open("out","w")
 
    p = getPrime(512)
    n=pow(p,random.randint(3,5))
    e = getPrime(100)
    f.write("n:"+hex(n)+"\n")
    f.write("e:"+hex(e)+"\n")
    c=pow(hex_msg,e,n)
    f.write("encrypted flag is:"+hex(c)+"\n")
    f.close()


if __name__ == "__main__":
    rsaEncode()

