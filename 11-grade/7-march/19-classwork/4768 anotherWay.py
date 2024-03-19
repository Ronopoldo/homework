from itertools import *


def f(x):
    P = 1 <= x <= 99
    Q = 25 <= x <= 43
    A = a1 <= x <= a2
    return (Q) <= (((not P) and (Q)) <= A)


Ox = [i / 4 for i in range(24 * 4, 75 * 4 + 4)]

answers = []

for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        answers.append(a2 - a1)

print(min(answers))
