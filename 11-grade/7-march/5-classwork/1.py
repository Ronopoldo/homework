'''
1. zxy
2. zwyx
3. yzwx
4. wzyx
5. 4
6. ywzx
7. zywx
'''




from itertools import *

def f(x, y, z):
    return ((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z))

for t in product([1,0], repeat = 1):
    table = [
        (0, 0, 0),
        (1, 0, 0),
        (1, 0, 1)
    ]

if len(table) == len(set(table)):
    for p in permutations('xyz'):
        if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
            print(p)

#zxy


