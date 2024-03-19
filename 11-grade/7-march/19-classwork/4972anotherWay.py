from itertools import *

def f(x):
    P = 25 <= x <= 50
    Q = 54 <= x <= 75
    A = a1 <= x <= a2
    return Q <= ((P == Q) or ((not P) <= A))

Ox = [i/4 for i in range(24*4, 75*4)]

answers = []

for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        answers.append(a2-a1)


print(min(answers))