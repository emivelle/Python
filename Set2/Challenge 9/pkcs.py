def pkcs7_pad(data, block_size):
    pad_len = block_size - len(data) % block_size
    return data + bytes([pad_len] * pad_len)

def pkcs7_unpad(data):
    return data[:-data[-1]]

text = b"YELLOW SUBMARINE"
padded = pkcs7_pad(text, 20)
print("Padded:  ", padded)
print("Unpadded:", pkcs7_unpad(padded))