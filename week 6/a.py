n = int(input())
a = map(int, input().split(maxsplit = n))
prod = 1
b = list(a)
for i in range(n):
    prod *= b[i]
print(float(prod))