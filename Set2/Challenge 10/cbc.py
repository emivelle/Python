from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

def xor(a, b): return bytes(x ^ y for x, y in zip(a, b))
def unpad(data): return data[:-data[-1]]

key = b"YELLOW SUBMARINE"
iv = b"\x00" * 16

with open("10.txt") as f:
    ciphertext = base64.b64decode(f.read())

cipher = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
plaintext = b""

for i in range(0, len(ciphertext), 16):
    block = ciphertext[i:i+16]
    decrypted = cipher.update(block)
    plaintext += xor(decrypted, iv)
    iv = block

print(unpad(plaintext).decode("utf-8", errors="replace"))
