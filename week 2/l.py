s = input()
l = []
for i in range(len(s)):
    if s[i] == "(" or s[i] == "[" or s[i] == "{":
        l.append(s[i])
    elif s[i] == ")" or s[i] == "]" or s[i] == "}":
        if len(l) != 0:
            if l[-1] == "(" and s[i] == ")" or l[-1] == "[" and s[i] == "]"  or l[-1] == "{" and s[i] == "}":
                l.pop(-1)
            else:
                l.append(s[i])
if len(l) != 0:
    print("No")
else:
    print("Yes")