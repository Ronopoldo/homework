def f(s, m):
    if s == 0: return (m % 2)== 0
    if m == 0: return 0

    if s >= 5:
        h = [
            f(s - 5, m - 1),
            f(s // 3, m - 1)
        ]
    else:
        h = [s // 3, m - 1]

    if ((m - 1) % 2) == 0:
        return any(h)
    else:
        return all(h)

for s in range(1, 300):
    if f(s, 4):
        print(s)


print(f(28,4))