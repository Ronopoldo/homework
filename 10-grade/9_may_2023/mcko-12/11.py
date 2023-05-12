# from sys import setrecursionlimit
#
#
# setrecursionlimit(8192)
#
#
#
#
#
#
# def f(b,e):
#     if b > e or b == 36: return 0
#     if b == e: return 1
#     if b < e: return f(b + 3, e) + f(b + 5, e) + f(b * 3, e)
#
# print(f(3,24) * f(24,40))








def f(b,e):
    if b > e or b == 36 : return 0
    if b == e: return 1
    if b < e: return f(b + 3, e) + f(b + 5, e) + f(b * 3, e)


print(f(3, 24) * f(24,40))