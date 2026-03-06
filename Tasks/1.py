import re
txt = ["a", "ab", "abb", "abbb", "ac", "ba"]
pt = r"ab*"
for s in txt:
    if re.fullmatch(pt, s):
        print(s, "match")
    else:
        print(s, "no match")