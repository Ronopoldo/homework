def f(s, m):
    if s >= 25:
        if s <= 45:
            return m % 2 == 0
        else:
            return m % 2 != 0
    if m == 0: return 0

    h = [
        f(s + 1, m - 1),
        f(s * 2, m - 1)
    ]

    if (m-1) % 2:
        return all(h)
    else:
        return any(h)

for s in range(1, 25):
    if f(s, 3) and not f(s, 1):
        print(s)