def f(s1, s2, m):
    if (s1 + s2) >= 45: return m % 2 == 0
    if m == 0: return 0

    h = [
        f(s1 + s2, s2, m - 1),
        f(s1, s2 + s1,  m - 1)

    ]

    if (m-1) % 2:
        return all(h)
    else:
        return any(h)

for s in range(1, 45):
    if f(s, s, 4):
        print(s)