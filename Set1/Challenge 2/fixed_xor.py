import base64

def fixed_xor(hex1, hex2):
    b1 = bytes.fromhex(hex1)
    b2 = bytes.fromhex(hex2)
    result = bytes(a ^ b for a, b in zip(b1, b2))
    return result.hex()

def main():
    hex1 = '1c0111001f010100061a024b53535009181c'
    hex2 = '686974207468652062756c6c277320657965'

    result = fixed_xor(hex1, hex2)
    print(result)

if __name__ == "__main__":
    main()