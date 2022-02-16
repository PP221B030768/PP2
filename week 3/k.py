import itertools
def permut(s):
    perm = itertools.permutations(s)
    for i in perm:
        print(*i)
s = input()
permut(s)