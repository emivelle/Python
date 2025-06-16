import base64

def hex_to_base64(hex_str):
    bytes_data = bytes.fromhex(hex_str.strip())
    b64_str = base64.b64encode(bytes_data).decode('utf-8')
    return b64_str

def main():
    hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    b64_result = hex_to_base64(hex_str)
    print(b64_result)

if __name__ == "__main__":
    main()