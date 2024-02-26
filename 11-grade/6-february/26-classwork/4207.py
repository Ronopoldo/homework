def f(s1, s2, s3, m):
    if (s1 + s2 + s3) >= 73: return m % 2 == 0
    if m == 0: return 0

    h = [
        f(s1 + 3, s2, s3, m - 1),
        f(s1 + 13, s2, s3,   m - 1),
        f(s1 + 23, s2, s3,  m - 1),
        f(s1 , s2+ 3, s3, m - 1),
        f(s1, s2 + 13, s3,   m - 1),
        f(s1, s2 + 23, s3,  m - 1),
        f(s1, s2, s3 + 3, m - 1),
        f(s1, s2, s3 + 13,   m - 1),
        f(s1 , s2, s3 + 23,  m - 1),

    ]

    if (m-1) % 2:
        return all(h)
    else:
        return any(h)

for s in range(1, 23):
    if f(2, s, 2 *s, 3) and not f(2, s, 2 *s, 1):
        print(s)