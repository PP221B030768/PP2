n = int(input())
l = list("")
for i in range(n):
    num, disc = input().split()
    if num == "1":
        l.append(disc)
    else:
        l.remove(l[0])
print(*l)