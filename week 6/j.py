mylist = list(map(str, input().split()))
#mylist = ['a', 'b', 'c', 'd']
with open('input.txt', 'w') as wr:
    for item in mylist:
        wr.write('%s\n' %item)