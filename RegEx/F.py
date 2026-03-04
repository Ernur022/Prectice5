import re
txt = "The rain in Spain 123"
x = re.findall("[a-m]", txt)
print(x)


y = re.findall(r"\d", txt)
print(y)


z = re.findall("Sp..n", txt)
print(z)


c = re.findall("^The", txt)
if x:
    print("Yes")
else:
    print("No")



v = re.findall("Go$", txt)
if v:
    print("Yes")
else:
    print("No")



b = re.findall("Sp.*n", txt)
print(b)



n = re.findall("Sp.+n", txt)
print(n)



m = re.findall("Sp.?n", txt)
print(m)



a = re.findall("Sp.{2}n", txt)
print(a)



s = re.findall("Spain|France", txt)
if s:
    print("Yes")
else:
    print("No")