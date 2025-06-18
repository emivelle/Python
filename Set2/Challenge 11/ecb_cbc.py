import os, random
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def pad(x): p=16-len(x)%16; return x+bytes([p]*p)
def xor(a,b): return bytes(x^y for x,y in zip(a,b))

def oracle(data):
    k = os.urandom(16)
    data = pad(os.urandom(random.randint(5,10)) + data + os.urandom(random.randint(5,10)))
    if random.randint(0,1):
        iv = os.urandom(16)
        return Cipher(algorithms.AES(k), modes.CBC(iv)).encryptor().update(data), "CBC"
    else:
        return Cipher(algorithms.AES(k), modes.ECB()).encryptor().update(data), "ECB"

def detect(ct):
    blocks = [ct[i:i+16] for i in range(0,len(ct),16)]
    return "ECB" if len(blocks) > len(set(blocks)) else "CBC"

for _ in range(10):
    pt = b"A"*64
    ct, mode = oracle(pt)
    print(f"Detecté: {detect(ct)} | Actuel: {mode}")