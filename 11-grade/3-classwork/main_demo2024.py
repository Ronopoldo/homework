from fnmatch import *

for x in range(0, 10 ** 10 + 1, 2024):
    if fnmatch(str(x), '1?2157*4'):
        print(x, x // 2024)
