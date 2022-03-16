import os
file = open('f.txt', 'r')
content = file.read()
cnt = 0 
for i in content:
    if i == '\n':
        cnt += 1
cnt += 1
print(cnt)