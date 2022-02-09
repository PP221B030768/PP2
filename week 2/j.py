n = int(input())
a = []
for i in range(n):
    password = input()
    if password.isalpha() == False:
        for j in password:
            if j.isupper():
                for i in password:
                    if i.islower():
                        if password not in a:
                            a.append(password)
print(len(a))
a.sort()
for i in range(len(a)):
    print(a[i])