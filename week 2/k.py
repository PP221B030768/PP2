str = input()
st = set(str.split())
print(len(st))
l = list(st)
l.sort()
for i in l:
    if i.isalpha():
        print(i)
    else:
        print(i[:-1])