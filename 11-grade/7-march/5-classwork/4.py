from itertools import *


def f(x, y, z, w):
    return (w <= y) and ((x <= z) == (y <= x))


for t in product([1, 0], repeat=4):
    table = [
        (t[0], 1, t[1], 0),
        (0, t[2], 1, t[3]),
        (0, 1, 0, 1)
    ]

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)

# wzyx



