#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pwn import *
from Crypto.Util.number import *
from fractions import Fraction
import base64
# 输入为靶机 IP 和端口以及要验证的 flag
HOST = sys.argv[1]
PORT = sys.argv[2]
FLAG = sys.argv[3]

def get_treasure(sh):
    sh.sendafter(b'4. exit\n>', "3".encode())
    sh.recvline()
    n=int(sh.recvline().decode())
    flag_enc=int(sh.recvline().decode())
    return (n,flag_enc)
def get_flag(sh,n,c):
    R = n%4
    j = 1
    exp4 = 4
    length = n
    low_bound = Fraction(0,1)
    while length>1:
        tmp_c = (pow(exp4,0x10001,n)*c) % n
        sh.sendafter(b'4. exit\n>', "1".encode())
        sh.sendafter(b'What do you want to say to God:', str(tmp_c).encode())
        card=sh.recvline().decode()
        print(card.strip("\n"))
        if card=="You got one N!\n":
            r=0
        elif card=="You got one R!\n":
            r=1
        elif card=="You got one SR!\n":
            r=2
        else:
            r=3
        k = (-r* inverse(R,4)) % 4
        low_bound += Fraction(k*n,exp4)
        exp4 *= 4
        length = length//4
        print(r,j)
        j +=1
    return int(low_bound)
# exp 函数
def exp(ip, port):
    sh = remote(ip,port)
    n,flag_enc=get_treasure(sh)
    print(n,flag_enc)
    flag=get_flag(sh,n,flag_enc)
    return long_to_bytes(flag)

if __name__ == '__main__':
    flag = exp(HOST, PORT)
    flag=flag[6:-1]
    # 比较得出的 flag 是否是想要的 flag
    print("flag is :{}".format(flag))
    assert flag == FLAG
    print("Pass!")