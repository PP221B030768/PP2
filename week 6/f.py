import os
print('Only directories:')
with os.scandir('er/') as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)
print('Only files:')
with os.scandir('er/') as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)
print('All directories and files:')
with os.scandir('er/') as entries:
    for entry in entries:
        print(entry)