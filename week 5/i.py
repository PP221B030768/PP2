import re
s = input()
x = re.sub('[A-Z]', r'\1', s)
print(x)