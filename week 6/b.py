str = input()
up_cnt = 0
low_cnt = 0
for i in str:
    if i >= 'A' and i <= 'Z':
        up_cnt += 1
    elif i >= 'a' and i <= 'z':
        low_cnt += 1
print(int(up_cnt), low_cnt)