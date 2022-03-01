def squares(a, b):
    num = a
    while num <= b:
        yield num*num
        num += 1

a, b = map(int, input().split())

for i in squares(a, b):
    print(i, end = ' ')
print()
for it in range(a, b+1):
    print(it*it, end = ' ')