def f(s, m):
    if s >= 37: return m % 2 == 0
    if m == 0: return 0

    h = [
        f(s + 1, m - 1),
        f(s + 2, m - 1),
        f(s * 3, m - 1)
    ]

    if (m-1) % 2:
        return all(h)
    else:
        return any(h)

for s in range(1, 37):
    if f(s, 3) and not f(s, 1):
        print(s)