def xor_with_key(cipher_bytes, key):
    return ''.join(chr(b ^ key) for b in cipher_bytes)

def main():
    hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    cipher_bytes = [int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2)]

    best_score = -1
    best_result = ""
    best_key = None

    for key in range(32, 127):  
        result = xor_with_key(cipher_bytes, key)
        

        score = 0
        for c in result.lower():
            if c in 'etaoinshrdlu ':
                score += 1

        if score > best_score:
            best_score = score
            best_result = result
            best_key = key

    print(f"Clé trouvée : {chr(best_key)}")
    print(f"Texte : {best_result}")

if __name__ == "__main__":
    main()
