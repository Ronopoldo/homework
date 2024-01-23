from itertools import *

def f(x,y,z,w):
    return ((not x) and (not y)) or (y == z) or (not w)

for t in product([0, 1], repeat = 4):
    table = [
        (0, t[0], 0, 1),
        (t[1], 0, t[2], 1),
        (0, 1, 1, t[3])
    ]

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            temp = []
            for r in table:
                if f(**dict(zip(p, r))) == 0:
                    temp.append(0)

                if temp == [0,0,0]:
                    print(p)
