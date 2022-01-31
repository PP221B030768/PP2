a = input()
b = input()
if b == 'k':
    c = int(input())
    d = float(int(a)/1024)
    print(round(d, c))
if b == 'b':
    d = int(a)*1024
    print(d)