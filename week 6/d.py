import time
num = int(input())
sec = int(input())
ms = sec/1000
time.sleep(ms)
print('Square root of', num, 'after', sec, 'miliseconds is', pow(num, 0.5))