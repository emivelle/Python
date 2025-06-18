from PIL import Image
from collections import Counter
import matplotlib.pyplot as plt

img_ecb = Image.open("image_ecb_crypto.png")
img_bytes_ecb = img_ecb.tobytes()

blocks = [img_bytes_ecb[i:i+16] for i in range(0, len(img_bytes_ecb), 16)]

counter = Counter(blocks)

print(f"Nombre total de blocs : {len(blocks)}")
print(f"Nombre de blocs uniques : {len(counter)}")
print(f"Nombre de blocs répétés : {sum(1 for c in counter.values() if c > 1)}")

plt.hist(counter.values(), bins=range(1, max(counter.values()) + 1))
plt.title("Fréquence des blocs (mode ECB)")
plt.xlabel("Occurrences")
plt.ylabel("Nombre de blocs")
plt.show()
