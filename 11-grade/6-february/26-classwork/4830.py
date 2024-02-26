def f(s, m, lastOne):
    if s >= 62: return m % 2 == 0
    if m == 0: return 0

    h = []
    if lastOne != '+1': h += [f(s + 1, m - 1, '+1')]
    if lastOne != '+2': h += [f(s + 2, m - 1, '+2')]
    if lastOne != '*3': h += [f(s * 3, m - 1, '*3')]


    if (m-1) % 2 == 0:
        return any(h)
    else:
        return all(h)

for s in range(1, 62):
    if f(s, 3, 'e') and not f(s, 1, 'e'):
        print(s)