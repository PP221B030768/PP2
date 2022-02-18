def prime(L):
    prime_list = []
    for i in L:
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int((int(i))/2)+1):
                if int(i) % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
import sys
L = list(map(str, sys.stdin.read().split()))
print(*prime(L))