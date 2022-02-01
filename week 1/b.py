a = str(input())
s = 0
for i in a:
    s += ord(i)
if s > 300:
    print("It is tasty!")
else:
    print("Oh, no!")