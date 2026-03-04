import re
txt = "The rain in Spain in 11:45"



x = re.findall("[Tan]", txt)
print(x)



y = re.findall("[a-n]", txt)
print(y)



z = re.findall("[^arn]", txt)
print(z)


c = re.findall("[0123]", txt)
print(c)


v = re.findall("[0-9]", txt)
print(v)


b = re.findall("[0-5][0-9]", txt)
print(b)



n = re.findall("[a-zA-Z]", txt)
print(n)