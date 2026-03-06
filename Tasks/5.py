import re
txt = ["a", "ab", "a684b", "aGdswdb", "acb"]
pt = r"a.*b"
for s in txt:
    if re.fullmatch(pt, s):
        print(s, "match")
    else:
        print(s, "no match")