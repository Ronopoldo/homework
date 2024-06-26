from itertools import *


def f(x, y, z, w):
    return ((not x) and (not y)) or (y == z) or w


for t in product([0, 1], repeat=4):
    t = [
        (t[0], t[1], 1, t[2]),
        (1, 0, t[3], 1),
        (0, 0, 1, 1)
    ]

    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(p)
