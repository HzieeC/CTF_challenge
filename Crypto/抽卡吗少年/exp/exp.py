import random, time
from randcrack import RandCrack
from pwn import *

rc = RandCrack()
random.seed(time.time())
def guess(sh):
    for i in range(624):
        sh.sendafter(b'5. exit\n', "1".encode())
        guess__=""
        for j in range(8):
            sh.sendafter(b'Please enter your choice by 0-15:', "0".encode())
            rec = sh.recvline().decode()
            s=rec.split("]")[0][2:-1]
            card_library=s.split("', '")
            guess_=card_library.index("SSR")
            guess__+=hex(guess_)[2:].strip("L")
            print(card_library)
            print(guess_)
        rc.submit(int(guess__,16))
    key=[]
    for i in range(20):
        key.append(rc.predict_getrandbits(32))
    return key
def get_ssr(sh,key):
    for i in key:
        sh.sendafter(b'5. exit\n', "1".encode())
        for j in hex(i)[2:].strip("L").zfill(8):
            sh.sendafter(b'Please enter your choice by 0-15:', str(int(j,16)).encode())
if __name__ == '__main__':
    add = "0.0.0.0"
    port = 9999
    sh = remote(add,port)
    key=guess(sh)
    get_ssr(sh,key)
    sh.interactive()