a, b = map(int, input().split())
c = 0
if a > 1:
    for i in range (3,int(a/2)+1):
        if a%i == 0:
            c+=1
if c == 0 and a < 500 and b%2 == 0:
    print("Good job!")
else:
    print("Try next time!")
# d = int(input())
# n = int(input())
# if d>500 or n%2==1:
#     print("b")
# if d<500 and n%2==0:
#     def Check(d):
#         if d == 2 or d == 3: 
#             return True
#         if d<2: 
#             return False
#         for i in range(3, int(d/2)+1):
#             if d%i==0:
#                 return False
#         return True
#     if Check:
#         print("Good job!")
#     else:
#         print("Try next time!")