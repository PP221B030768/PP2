import re
s = input()
print(re.findall(r'ab{2,3}', s))