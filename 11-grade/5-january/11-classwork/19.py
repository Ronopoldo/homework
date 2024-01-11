# def f(s, m):
#     if s >= 301: return (m % 2) == 0
#     if m == 0: return 0
#     h = [
#         f(s + 3, m - 1),
#         f(s * 5, m - 1)
#     ]
#
#     if (m - 1) % 2 == 0:
#         return any(h)
#     else:
#         return all(h)
#
#
# for s in range(301):
#     if f(s, 4):
#         print(s)







def f(s1, s2, m):
    if ((s1 + s2) >= 45): return (m % 2) == 0
    if m == 0: return 0
    h = [
        f(s1 + 2, s2, m - 1),
        f(s1 * 3, s2, m - 1),
        f(s1, s2 + 2, m - 1),
        f(s1, s2 * 3, m - 1)
        ]

    if (m - 1) % 2 == 0:
        return any(h)
    else:
        return any(h)


for s2 in range(40):
    if f(4, s2, 2):
        print(s2)