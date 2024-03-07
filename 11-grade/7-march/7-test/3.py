def f(s, m):
    if s >= 36:
        if s < 60:
            return m % 2 == 0
        else:
            return m % 2 != 0
    if m == 0: return 0
    h = [
        f(s + 1, m - 1),
        f(s * 2, m -1),
        f(s * 3, m - 1)
    ]

    if (m - 1) % 2 == 0:
        return any(h)
    else:
        return all(h)


for s in range(35):
    if f(s, 4) and not f(s, 2):
        print(s)

# 19) 34
# 20) 1
# 21) 11_32

