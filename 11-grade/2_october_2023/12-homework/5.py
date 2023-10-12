from fnmatch import *

for i in range(0, 10 ** 9, 23):
    if fnmatch(str(i), '12345?7?8'):
        print(i, i // 23)
