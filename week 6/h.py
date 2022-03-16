import os
if os.access('er/', os.F_OK):
    with os.scandir('er/') as entries:
        print('Files:')
        for entry in entries:
            if entry.is_file():
                print(entry.name)
    with os.scandir('er/') as entries:
        print('Diretories:')
        for entry in entries:
            if entry.is_dir():
                print(entry.name)