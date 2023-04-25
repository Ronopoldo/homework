#from sys import *

#print(getrecursionlimit())
#setrecursionlimit()

# def f(n):
#     if  n == 1: return 1
#     if n > 1: return n * f(n-1)


# def f(n):
#     out = 1
#     while n > 1:
#         out = out * (n - 1)
#         n= n - 1
#     return out
#
# print(f(2023) - f(2020))


from functools import *

@lru_cache(None)


def f(n):
    if  n == 1: return 1
    if n > 1: return n * f(n-1)


for n in range(2,10000):
    f(n)

print(f(2023) / f(2020))