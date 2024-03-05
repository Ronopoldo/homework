from itertools import *

gammaArray = ["and", "==", "<=", "or"]

def f(c, a, d, b, gamma):
    return ((a and b) == (not (c))) and (eval(f'b {gamma} d'))


for gamma in gammaArray:
    answers = [
        f(1, 0, 0, 0, gamma),
        f(1, 0, 1, 0, gamma),
        f(1, 0, 1, 1, gamma),
        f(1, 1, 0, 0, gamma)
    ]

    if all(answers):
        print(gamma)



