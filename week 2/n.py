l = list("")
while True:
    n = int(input())
    if n == 0:
        break
    else:
        l.append(n)
if len(l)%2 == 0:
    for i in range(int(len(l)/2)):
        print(l[i]+l[n-i-1], end = " ")
else:
    for i in range(int(len(l)/2)):
        print(l[i]+l[n-i-1], end = " ")
    print(l[int(len(l)/2)])