def Histogram(L):
    for i in L:
        for j in range(0, int(i)):
            print("*", end = "")
        print()
import sys
L = list(map(str, sys.stdin.read().split()))
Histogram(L)