from itertools import *
def f(x,y,z,w):
    return (((y <= x) == (x <= w)) and (z or x))


for a in product([0, 1], repeat = 6):
    table = [(0, a[0], a[1], 0),
            (0,0,0,a[2]),
            (a[3],a[4],0,a[5])]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r)))for r in table] == [0, 0, 0]:
                print(p)



