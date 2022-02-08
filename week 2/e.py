import sys

L = list(map(str, sys.stdin.read().split()))
r = 0
i = 0
while i < int(L[0]):
    r = (int(L[1])+2*i)^r
    i = i+1
print(r)