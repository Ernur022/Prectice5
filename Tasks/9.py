import re 
txt = "HelloWorldPython"
rs = re.sub(r"([A-Z])", r" \1", txt).strip()
print(rs)