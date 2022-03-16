import os
print('existance:', os.access('er/', os.F_OK))
print('readability:', os.access('er/', os.R_OK))
print('writability:', os.access('er/', os.W_OK))
print('executability:', os.access('er/', os.X_OK))