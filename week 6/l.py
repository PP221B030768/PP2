with open ('f.txt', 'r') as re:
    data = re.read()
with open ('copy.txt', 'w') as wr:
    wr.write(data)