from itertools import *


def f(x, y, z, w):
    return ((x <= (y and w)) and (z <= (x or y))) != w


for t in product([1, 0], repeat=4):
    table = [
        (t[0], 1, t[1], 0),
        (t[2], 1, 1, 1),
        (1, t[3], 1, 0)
    ]

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)

# ywzx

