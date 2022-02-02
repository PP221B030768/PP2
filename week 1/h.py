s = input()
t = input()
x = s.find(t)
y = s.rfind(t)
if x == y:
    print(x)
else:
    print(x, end = " ")
    print(y)