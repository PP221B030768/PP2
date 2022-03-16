def palin(str):
    rev = []
    for i in range(len(str)-1, -1, -1):
        rev.append(str[i])
    rev = ''.join(rev)
    if rev == str:
        return True
    else:
        return False

str = input()
if palin(str):
    print('Yes')
else:
    print('No')