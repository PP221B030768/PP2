def delim(n):
    num = 0
    while num <= n:
        if num%3 == 0 and num%4 == 0:
            yield num
        num += 1

s = ""

for i in delim(int(input())):
    s += str(i)
    s += ', '

print(s[:-2])