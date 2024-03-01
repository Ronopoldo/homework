from itertools import *
def f1(x, y, z, w):
    return ((w <= z) == (y <= x))

def f2(x, y, z, w):
    return (w <= z) and ((not(x)) == y)

for t in product([0, 1], repeat=3):
    table = [(t[0], 0, 0, 0),
             (t[1], 0, 1, 1),
             (0, 0, t[2], 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            for t1 in product([0, 1], repeat=2):
                if ([f1(**dict(zip(p, r))) for r in table] == [0, t1[0], 0]):
                    if ([f2(**dict(zip(p, r))) for r in table] == [t1[1], 0, 1]):
                        print(p)