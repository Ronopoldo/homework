from itertools import *


def f(x, y, z, w):
    return x and (y <= z) or w

answer = []

for t in product([1, 0], repeat=6):
    table = [
        (1, 0, t[0], 1),
        (t[1], 0, 1, t[2]),
        (t[3], 0, t[4], t[5])
    ]

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                answer.append(p)
                print(p)

print(len(set(answer)), len(answer))

# 4



