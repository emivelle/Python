def repeating_key_xor(plaintext, key):
    result = []
    key_bytes = key.encode()
    for i in range(len(plaintext)):
        xor_byte = ord(plaintext[i]) ^ key_bytes[i % len(key)]
        result.append(f"{xor_byte:02x}")  # convertit en hex avec 2 chiffres
    return ''.join(result)

def main():
    text = (
        "Burning 'em, if you ain't quick and nimble\n"
        "I go crazy when I hear a cymbal"
    )
    key = "ICE"
    encrypted = repeating_key_xor(text, key)
    print(encrypted)

if __name__ == "__main__":
    main()
