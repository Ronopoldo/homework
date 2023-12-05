from itertools import *
def f1(x, y, z, w):
    return (x or (not y)) == (z <= w)

def f2(x, y, z, w):
    return (not x == y) and (z <= w)

for t in product([0, 1], repeat=3):
    table = [(t[0], 0, 0, 0),
             (0, 0, t[1], 0),
             (t[2], 1, 1, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f1(**dict(zip(p, r))) for r in table] == [0, 0, 0 or 1]:
                # if [f2(**dict(zip(p, r))) for r in table] == [0 or 1, 1, 0]:
                print(p)

'''
ywxz
zxyw
'''
# zxyw