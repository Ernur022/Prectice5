import re
txt = "Hello my Name is Ernur"
pt = r"\b[A-Z][a-z]+\b"
r = re.findall(pt, txt)
print(r)