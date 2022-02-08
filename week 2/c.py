n = int(input())
for i in range(n): 
    for j in range(n): 
        if i == j:
            print(i*j, end = " ")
        if i == 0 and j != 0:
            print(j, end = " ")
        if j == 0 and i != 0:
            print(i, end = " ")
        if i != 0 and j != 0 and i != j:
            print("0", end = " ")
    print()