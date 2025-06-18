with open("8.txt", "r") as f:
    lines = f.readlines()

max_score = 0
ecb_line = ""

for line in lines:
    line = line.strip()
    data = bytes.fromhex(line)
    blocks = [data[i:i+16] for i in range(0, len(data), 16)]
    score = len(blocks) - len(set(blocks))  
    if score > max_score:
        max_score = score
        ecb_line = line

print("Ligne en ECB :")
print(ecb_line)
