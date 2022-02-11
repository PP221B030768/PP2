n = int(input())
d = {}
for i in range(n):
    name, num = map(str, input().split())
    if name in d.keys:
        d[name] += num
    else:
        d[name] += num
l1 = list(d.values())
l2 = list(d.keys())
l1.sort()
l2.sort()
mx = l1[-1]
for i in l2:
    if max-d[i] == 0:
        print(i, "is lucky!")
    else:
        print(i, "has to receive", max-d[i]< "tenge")