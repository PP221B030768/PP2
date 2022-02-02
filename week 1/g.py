def perevod(n):
    s = 0
    for i in range(0, len(n)):
        s += 2**(len(n)-i-1) * int(n[i])
    return s
n = input()
p = perevod(n)
print(p)