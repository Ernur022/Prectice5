import re
txt = "Hello, World. KBTU is good"
r = re.sub(r"[ ,.]", ":", txt)
print(r)