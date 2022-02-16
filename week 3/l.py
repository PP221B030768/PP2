def Reverse(l):
    for i in range(len(l)):
        print(l[len(l)-i-1], end = " ")
a = input()
l = list(a.split())
Reverse(l)