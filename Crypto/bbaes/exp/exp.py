import base64
from Crypto.Cipher import AES
c="j5e0IruHWOwr7ilf92ppHgXqZ//xyTWloveQk+Jml6E="
key = 'xgctf{not_flag~}'
m = AES.new(key, AES.MODE_ECB)
print(m.decrypt(base64.b64decode(c)))