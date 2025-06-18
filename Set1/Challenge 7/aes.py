from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

with open('fichier.txt', 'r') as f:
    b64data = f.read()

ciphertext = base64.b64decode(b64data)
key = b"YELLOW SUBMARINE"

cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()

print(plaintext.decode('utf-8', errors='replace'))
