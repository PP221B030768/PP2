def Palindrome(s):
    t = s[::-1]
    if t == s:
        return True
    else:
        return False
s = input()
if Palindrome(s):
    print("Yes")
else:
    print("No")