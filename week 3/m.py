import sys
def Check(L):
    for i in range(len(L)-1):
        if L[i] == '3' and L[i+1] == '3':
            return True
    return False
L = list(map(str, sys.stdin.read().split()))
print(Check(L))