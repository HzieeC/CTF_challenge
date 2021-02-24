from Crypto.Util import number
import random
from string import ascii_letters, digits
from flag import FLAG
from hashlib import sha256
def genkey():
    # DSA
    N=128
    L=1024-N-1
    q = number.getPrime(N)

    while True:
        t = random.getrandbits(L)
        p = (t * 2*q + 1)
        if number.isPrime(p):
            break

    e = (p-1) // q
    g = pow(2, e, p)

    x = random.randint(1, q-1)
    y = pow(g, x, p)

    return {'y':y, 'g':g, 'p':p, 'q':q, 'x':x}

def sign(m, key):
    g, p, q, x = key['g'], key['p'], key['q'], key['x']

    k = random.randint(1, q-1)
    print(f"k = {k}")

    Hm = int.from_bytes(sha256(m.encode()).digest(), 'big')

    r = pow(g, k, p) % q
    s = (number.inverse(k, q) * (Hm + x*r)) % q
    return (r, s)

def verify(m, sig, key):
    r, s = sig
    y, g, p, q = key['y'], key['g'], key['p'], key['q']
    if not (0 < r < q) or not (0 < s < q):
        return False

    Hm = int.from_bytes(sha256(m.encode()).digest(), 'big')
    w = number.inverse(s, q)
    u1 = (w * Hm) % q
    u2 = (w * r) % q
    v = ( (pow(g, u1, p) * pow(y, u2, p)) % p ) % q

    return v == r

def _is_valid_name(name):
    if not (0 < len(name) <= 20):
        print("Invalid username length!")
        return False

    for c in name:
        if c not in ascii_letters + digits:
            print("Invalid character in username!")
            return False

    if name == "xgctf":
        print("Username can't be 'xgctf'")
        return False

    return True

def sign_up(key):
    name = input("Please input your username: ")
    if not _is_valid_name(name):
        return

    (r, s) = sign(name, key)
    sig = name.encode() + r.to_bytes(20, 'big') + s.to_bytes(20, 'big')
    print(f"Here is your signature in hex: {sig.hex().upper()}")


def sign_in(key):
    data = input("Please send me your signature: ")
    try:
        data = bytes.fromhex(data)
    except ValueError:
        print("Invalid signature format!")
        return
    if not (40 < len(data) <= 60):
        print("Invalid signature length!")
        return

    (name, r, s) = (data[:-40].decode(), data[-40:-20], data[-20:])
    sig = map(lambda x: int.from_bytes(x, 'big'), (r, s))

    if not verify(name, sig, key):
        print("Wrong signature!")
        return

    print(f"Welcome, {name}")
    if name == "xgctf":
        print(f"The flag is {FLAG}")



menu = '''
1. sign up
2. sign in
3. exit\
'''

def main():
    try:
        print("Generating DSA parameters...")
        key = genkey()
        print(f"p = {key['p']}")
        print(f"q = {key['q']}")
        print(f"g = {key['g']}")
        print(f"y = {key['y']}")
        while True:
            print(menu)
            choice = input("$ ")

            if choice == "1":
                sign_up(key)

            elif choice == "2":
                sign_in(key)

            elif choice == "3":
                print("Bye!")
                return

            else:

                print("Invalid choice!")
                continue
    except:
        pass
if __name__ == "__main__":
    main()