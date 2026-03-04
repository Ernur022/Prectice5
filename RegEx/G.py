import re 
txt = "The rain in Spain 12 falls 45 mainly in the plain"


x = re.findall(r"\AThe", txt)
if x:
    print("Yes")
else:
    print("No")



y = re.findall(r"\bain", txt)
z = re.findall(r"ain\b", txt)
if y:
    print("Yes")
elif z:
    print("Yes2")
else:
    print("No")




c = re.findall(r"\Bain", txt)
v = re.findall(r"ain\B", txt)
print(c)
print(v)



b = re.findall(r"\d", txt)
print(b)



d = re.findall(r"\D", txt)
print(d)



s = re.findall(r"\s", txt)
print(s)



w = re.findall(r"/w", txt)
print(w)



q = re.findall(r"\Z", txt)
print(q)