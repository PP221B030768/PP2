import os
if os.access('qw/', os.F_OK):
    os.remove('qw/qq.txt')