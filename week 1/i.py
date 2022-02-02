n = int(input())
for i in range(0,n):
    a = str(input())
    x = a.find("@gmail.com")
    if x != -1:
        # for e in a:
        #     if e != "@":
        print(a[:-10])