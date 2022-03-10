import re
s = input()
t = re.findall(r'ab*', s)
print(t)