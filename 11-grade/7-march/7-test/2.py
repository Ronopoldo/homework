def f(s, m):
    if s >= 30: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s + 2, m - 1),
        f(s + 3, m - 1),
        f(s * 2, m -1)
    ]

    if (m - 1) % 2 == 0:
        return any(h)
    else:
        return all(h)


for s in range(30):
    if f(s, 4) and not f(s, 2):
        print(s)

# 19) 13
# 20) 4
# 21) 8 9