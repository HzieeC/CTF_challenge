#coding=utf-8
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
import base64
from flag import FLAG

BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

class AESCipher:

    def __init__(self, key):
        self.key=key.encode()
    def encrypt(self, raw):
        raw = pad(raw).encode()
        cipher = AES.new(self.key, AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(raw)).decode('utf8')

if __name__ == '__main__':
    flag = FLAG
    key = 'xgctf{not_flag~}'
    #调用加密函数 
    encrypted_text = AESCipher(key).encrypt(flag)
    f=open("out","w")
    f.write("加密后的值是:\n"+encrypted_text)
    f.close()