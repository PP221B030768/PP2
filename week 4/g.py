import math
num = int(input())
len = int(input())
area = (num * pow(len, 2))/(4 * math.tan(math.radians(360/(2 * num))))
print(int(area))