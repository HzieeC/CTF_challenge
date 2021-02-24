# -*- coding:utf-8 -*-
from pwn import *
from hashlib import sha256
from Crypto.Util import number


sh=remote("127.0.0.1",1234)#靶机地址和端口改为题目靶机地址和端口
sh.recvuntil("p = ")
p=int(sh.recvline().strip("\n"))
sh.recvuntil("q = ")
q=int(sh.recvline().strip("\n"))
sh.recvuntil("g = ")
g=int(sh.recvline().strip("\n"))
sh.recvuntil("y = ")
y=int(sh.recvline().strip("\n")) 
sh.recvuntil("$ ")
sh.sendline("1")
sh.recvuntil("Please input your username: ")
m="1"
sh.sendline(m)
sh.recvuntil("k = ")
k=int(sh.recvline().strip("\n")) 
sh.recvuntil("Here is your signature in hex: ")
sig=sh.recvline().strip("\n")[len(m)*2:]

r=int(sig[:40],16)
s=int(sig[40:],16)
Hm = int(sha256(m.encode()).digest().encode("hex"),16)
x=(number.inverse(r, q)*(k*s-Hm))%q
key={'y':y, 'g':g, 'p':p, 'q':q, 'x':x}
def sign(m, key,k):
    g, p, q, x = key['g'], key['p'], key['q'], key['x']

    Hm = int(sha256(m.encode()).digest().encode("hex"),16)

    r = pow(g, k, p) % q
    s = (number.inverse(k, q) * (Hm + x*r)) % q
    return (r, s)
def sign_up(name,key,k):

    (r, s) = sign(name, key,k)
    sig = name.encode('hex').upper() +hex(r)[2:].rjust(40, '0').upper() + hex(s)[2:].rjust(40, '0').upper()
    
    return sig

sig_xgctf=sign_up("xgctf",key,k)
sh.recvuntil("$ ")
sh.sendline("2")
sh.recvuntil("Please send me your signature: ")
sh.sendline(sig_xgctf)
sh.interactive()