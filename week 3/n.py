import sys
def spy_game(L):
    for i in range(0,len(L)):
        if L[i] == '0':
            for x in range(i+1,len(L)):
                if L[x] == '0':
                    for y in range(x+1,len(L)):
                        if L[y] == '7':
                            return True
    return False
L = list(map(str, sys.stdin.read().split()))
print(spy_game(L))