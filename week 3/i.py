def solve(numheads, numlegs):
    kur = (4 * numheads - numlegs)/2
    rab = numheads - kur
    return kur, "chicken and and", rab, "rabbits"
numheads = int(input())
numlegs = int(input())
print(*solve(numheads, numlegs))