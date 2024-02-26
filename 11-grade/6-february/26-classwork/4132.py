def f(s1, s2, m):
    if (s1 + s2) >= 70: return m % 2 == 0
    if m == 0: return 0

    h = [
        f(s1 + 1, s2, m - 1),
        f(s1 * 3, s2,  m - 1),
        f(s1 , s2 + 1, m - 1),
        f(s1 , s2 * 3, m - 1),

    ]

    if (m-1) % 2:
        return all(h)
    else:
        return any(h)

for s in range(1, 37):
    if f(6, s, 10):
        print(s)