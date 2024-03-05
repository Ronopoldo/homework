from itertools import *

def f(x, y, z, w):
    return (not x) and y and z or x and (not y) and (not w)

for t in product([1,0], repeat = 1):
    table = [
        (0, 0, 0, 1),
        (1, 0, 0, 1),
        (1, 0, 1, 0),
        (1, 1, 1, 0)
    ]

if len(table) == len(set(table)):
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1, 1]:
            print(p)

#zwyx