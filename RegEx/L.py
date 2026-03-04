import re
txt = "The rain in Spain"


x = re.search("rain", txt)
print(x.span())

print(x.string)

print(x.group())