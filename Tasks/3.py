import re 
txt = "hello my_name is Ernur i_like KBTU"
pt = r"\b[a-z]+_[a-z]+\b"
r = re.findall(pt, txt)
print(r)