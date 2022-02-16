def Unique(L):
    L1 = list("")
    for i in L:
        if i not in L1:
            L1.append(i)
    return L1
import sys
L = list(map(str, sys.stdin.read(). split()))
print(*Unique(L))