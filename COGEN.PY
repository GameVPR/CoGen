import random
import string
import os
import re

os.system('title CoGen V0.1.1')

# Dosya adını ve aranacak deseni belirle
filename = "codes.txt"
pattern = r"\b[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}\b"

with open(filename, 'w')as tmpf:
    tmpf.close()

# Dosyayı oku ve içindeki tüm metni bir dize olarak al
with open(filename, "r") as f:
    text = f.read()

# Desene uyan tüm kodları bul
matches = re.findall(pattern, text)

# Kod sayısını yazdır
print("\033[92m\u2713 {} codes found on starup.\033[0m".format(len(matches)))

# Counter for the number of codes written
count = 0
while True:
    try:
        code = '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(5))
    
        # Save the code to a file
        try:
            with open('codes.txt', 'a') as f:
                f.write(code + '\n')
                count += 1
                # print("\033[92m[\u2713] " + code + "\033[0m")
        except Exception as e:
            print("\033[91m[\u2717] " + code + "\033[0m")
            
        print("\033[92m\u2713 {} codes written.\033[0m".format(count), end='\r')
        
    except KeyboardInterrupt:
        print("\n\033[92m\u2713 {} keys in the file now.\033[0m".format(len(matches)+count))
        print("\033[31m{}\033[0m".format('> KEYGEN STOPPED <'))

        input('')
        break