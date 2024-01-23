from sys import *

setrecursionlimit(482194)

def f(s, e):
    if (s > e) or (s == 11) or (s == 12): return 0
    if (s == e): return 1
    if (s < e): return (f(s + 1, e) + f(s + 2, e) + f(s * 3, e))


print(f(1, 9) * f(9, 30))
