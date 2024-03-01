from itertools import *
def f1(x, y, z, w):
    return (x <= y) or ((not(w))  == z)

def f2(x, y, z, w):
    return (x <= y) == (w and (not(z)))

for t in product([0, 1], repeat=6):
    table = [(t[0], t[1], t[2], 0),
             (t[3], t[4], 0, 0),
             (t[5], 0, 0, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f1(**dict(zip(p, r))) for r in table] == [f2(**dict(zip(p, r))) for r in table]:
                print(p)