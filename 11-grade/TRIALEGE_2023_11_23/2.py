from itertools import *
def f(x, y, z, w):
    return (w <= x) and ((y <= z) == (x <= y))

for t in product([0, 1], repeat=4):
    table = [(0, 1, 1, 0),
             (1, t[0], t[1], 0),
             (t[2], 1, 0, t[3])
             ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1 , 1]:
                print(p)