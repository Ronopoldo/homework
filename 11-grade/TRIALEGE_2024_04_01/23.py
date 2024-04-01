from sys import *
setrecursionlimit(123678)

def f(s, e):
    if s > e: return 0
    if s == e: return 1
    return f(s + 1, e) + f(s * 2, e)

print(f(2, 23))




# def f(s, e):
#     if s > e: return 0
#     if s == e: return 1
#     if s < e: return f(s + 1, e) +  f(s * 2, e)
#
# print(f(2, 23))