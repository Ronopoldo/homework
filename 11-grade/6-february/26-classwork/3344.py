def f(s1, s2, m):
    if (s1 + s2) >= 30: return m % 2 == 0
    if m == 0: return 0

    h = [
        f(s1 + 1, s2, m - 1),
        f(s1 * 2, s2,  m - 1),
        f(s1 , s2 + 1, m - 1),
        f(s1 , s2 * 2, m - 1),

    ]

    if (m-1) % 2 == 0:
        return any(h)
    else:
        return all(h)

i = 0
# for k in range(1, 30):
#     for s in range(1, 30):
#         if f(k, s, 2) and (k + s < 30):
#             i+=1
#             print(k, s)
#
# print(i)


# for s in range(1, 30):
#     if f(6, s, 3) and not f(6, s, 1):
#         print(s)




for k in range(1, 30):
    for s in range(1, 30):
        if f(k, s, 4) and (k + s < 30) and not f(k,s,2):
            i+=1
            print(k, s)

print(i)
