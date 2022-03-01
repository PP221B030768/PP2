def sq_sequence(n):
    num = 0
    while num <= n:
        yield num*num
        num += 1

for num in sq_sequence(int(input())):
    print(num, end = " ")