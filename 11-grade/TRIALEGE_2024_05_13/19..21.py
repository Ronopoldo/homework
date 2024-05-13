def f(s, m):
    if s >= 63: return (m % 2) == 0
    if m == 0: return
    h = [
        f(s + 1, m - 1),
        f(s + 4, m - 1),
        f(s * 5, m - 1)
    ]

    if (m - 1) % 2 != 0:
        return all(h)
    else:
        return any(h)


for s in range(63):
    if f(s, 4) and (not f(s, 2)):
        print(s)