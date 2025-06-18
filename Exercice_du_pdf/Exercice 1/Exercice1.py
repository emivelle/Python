from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from PIL import Image
import os

img = Image.open("image.png")
img_bytes = img.tobytes()

pad_len = 16 - len(img_bytes) % 16
padded = img_bytes + bytes([pad_len] * pad_len)

# 3. AES-ECB
key = b'ThisIsA16ByteKey'  # 16 bytes
cipher = Cipher(algorithms.AES(key), modes.ECB())
encryptor = cipher.encryptor()
encrypted = encryptor.update(padded) + encryptor.finalize()

# 4. Sauvegarder l'image chiffrée
img_encrypted = Image.frombytes(img.mode, img.size, encrypted[:len(img_bytes)])
img_encrypted.save("image_ecb_crypto.png")
