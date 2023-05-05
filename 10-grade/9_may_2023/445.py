# def f(b, e):
#     if b > e: return 0
#     if b == e: return 1
#     if b < e: return f(b+1, e) + f(b * 2, e)
#
# def g(b, e):
#     if b > e: return 0
#     if b == e: return 1
#     if b < e: return f(b+1, e)
#
# print(f(4,24) - g(23, 24))


# def counter(b, e):
#     if b > e: return 0
#     if b == e: return 1
#     if b < e and b != 23: return f(b+1, e)
#
# def f(b, e):
#     if b > e: return 0
#     if b == e: return 1
#     if b < e and b != 23: return f(b+1, e) + f(b * 2, e)
#
#
# print(counter(4, 24))



def f(b, e):
    if b > e: return 0
    if b == e: return 1
    if b < e: return f(b+1, e) + f(b * 2, e)


print(f(4,11) + f(4, 22))