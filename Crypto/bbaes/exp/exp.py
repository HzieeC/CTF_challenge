#coding=utf-8
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class AESCipher:
    """
    Tested under Python 3.x and PyCrypto 2.6.1.
    """

    def __init__(self, key):
        #加密需要的key值
        self.key=key.encode()

    def decrypt(self, enc):
        #首先对已经加密的字符串进行解码
        enc = b64decode(enc)
        #通过key值，使用ECB模式进行解密
        cipher = AES.new(self.key, AES.MODE_ECB)
        return unpad(cipher.decrypt(enc)).decode('utf8')

if __name__ == '__main__':
    key = 'xgctf{not_flag~}'
    #调用加密函数 
    f=open("out","r")
    f.readline()
    encrypted_text=f.readline()
    f.close()
    #调用解密函数
    decrypted_text = AESCipher(key).decrypt(encrypted_text)
    print("flag:\n", decrypted_text)
    
