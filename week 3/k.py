from itertools import permutations
s = input()
def permut(s):
    return permutations(s)
perm = set(list(permutations(s)))
for i in perm:
    for j in i:
        print(j, end = '')
    print()