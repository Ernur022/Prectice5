import re
txt = "my_name_is_ernur"
pt = txt.split("_")
r = pt[0] + "".join(word.capitalize() for word in pt[1:])
print(r)