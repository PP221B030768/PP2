def even_sequence(n):
    num = 0
    while num <= n:
        if num%2 == 0:
            yield num
        num += 1

s = ""

for i in even_sequence(int(input())):
    s += str(i)
    s += ', '

print(s[:-2])