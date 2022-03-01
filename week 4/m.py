def reverse(n):
    num = n
    while num >= 0:
        yield num
        num -= 1

for i in reverse(int(input())):
    print(i, end = ' ')