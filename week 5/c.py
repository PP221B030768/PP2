import re
s = input()
#print(re.search('[a-z]+_[a-z]+$', s))
print(*re.findall('[a-z]*_*[a-z]',s))