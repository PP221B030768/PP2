d = {}
n = int(input())
for i in range(n):
    name, point = input().split()
    s = int(point)
    if name not in d.keys(): d[name] = s
    else: d[name] += s
l1 = list(d.values())
l2 = list(d.keys())
l1.sort()
l2.sort()
mx = l1[-1]
for i in l2:
    if mx-d[i] == 0:
        print(i, "is lucky!")
    else:
        print(i, "has to receive", mx-d[i], "tenge")