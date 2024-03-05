from itertools import *

def f(x, y, z, w):
    return (x and y) or (y == z) or w


for t in product([1, 0], repeat=5):
    table = [
        (1, t[0], t[1], 0),
        (0, 1, t[2], t[3]),
        (1, 0, t[4], 1)
    ]

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)

# zuwx

