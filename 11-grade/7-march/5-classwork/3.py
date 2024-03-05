from itertools import *

def f(x, y, z, w):
    return ((x <= z) and (z <=w)) or (y == (x or z))


for t in product([1, 0], repeat=7):
    table = [
        (t[0], 1, t[1], t[2]),
        (t[3], t[4], 1, 1),
        (t[5], 1, t[6], 1)
    ]

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)

# yzwx
