#1) 14

from itertools import *


def f(x, y, z, w):
    return (x and (not y)) or (x == z) or ( not w)


for t in product([0, 1], repeat=4):
    table = [(0, 1, 1, 0),
             (0, t[0], t[1], t[2]),
             (t[3], 1, 0, 1)
             ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0,0,0]:
                print(p)




