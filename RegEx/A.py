import re
txt = "Hello every one"
x = re.search("^Hello.*one$", txt)
if x:
    print("Yes")
else:
    print("NO")