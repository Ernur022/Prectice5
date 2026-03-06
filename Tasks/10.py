import re
txt = "myNameIsErnur"
rs = re.sub(r"([A-Z])", r"_\1", txt).lower()
print(rs)