def f(s1, s2, m):
    if s1 + s2>=259: return (m % 2) == 0
    if m == 0: return 0
    h = [
        f(s1+1, s2, m-1),
        f(s1*2, s2, m-1),
        f(s1, s2+1, m-1),
        f(s1, s2*2, m-1)
    ]

    if ((m - 1) % 2) == 0:
        return any(h)
    else:
        return all(h)

for s in range(1,242):
    if f(17, s, 4) and not f(17, s, 2):
        print(s)