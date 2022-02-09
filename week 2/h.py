import math
x, y = input().split()
n = int(input())
d = {}
s = []
for i in range(n):
    a, b = input().split()
    r = math.sqrt((int(y)-int(b))**2+(int(x)-int(a))**2) 
    s.append(r)
    d[r] = [a,b]
s.sort()
for i in s:
    print(*d[i])