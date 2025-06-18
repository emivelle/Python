from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from PIL import Image
import os

img = Image.open("image.png")
img_bytes = img.tobytes()

pad_len = 16 - len(img_bytes) % 16
padded = img_bytes + bytes([pad_len] * pad_len)

key = b'ThisIsA16ByteKey'

iv = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
encrypted = encryptor.update(padded) + encryptor.finalize()

img_encrypted = Image.frombytes(img.mode, img.size, encrypted[:len(img_bytes)])
img_encrypted.save("image_cbc_crypto.png")
