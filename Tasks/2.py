import re
txt = ["ab", "abb", "abbb", "abbbb", "a"]
pt = r"ab{2,3}"
for s in txt:
    if re.fullmatch(pt, s):
        print(s, "match")
    else:
        print(s, "no match")