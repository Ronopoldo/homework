from itertools import *

def f(x,y,z,w):
    return not(y <= x) or (z <= w) or (not z)

for i in product([0,1], repeat=7):
    t = [
        (i[0], 0, i[1], i[2]),
        (0, 1, i[3], i[4]),
        (1, i[5], i[6],0)
    ]

    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [0,0,0]:
                print(p)