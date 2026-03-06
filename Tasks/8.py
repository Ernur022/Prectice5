import re
txt = "HelloWorldPython"
r = re.split(r"(?=[A-Z])", txt)
r = [x for x in r if x]
print(r)