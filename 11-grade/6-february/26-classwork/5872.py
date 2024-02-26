def f(s, m, lastOne, preLastOne):
    if s >= 121: return m % 2 == 0
    if m == 0: return 0

    h = []
    if preLastOne != '+2': h += [f(s + 2, m - 1, '+2', lastOne)]
    if preLastOne != '+5': h += [f(s + 5, m - 1, '+5', lastOne)]
    if preLastOne != '+12': h += [f(s + 12, m - 1, '+12', lastOne)]
    if preLastOne != '*2': h += [f(s * 2, m - 1, '*2', lastOne)]


    if (m-1) % 2 == 0:
        return any(h)
    else:
        return all(h)

for s in range(1, 120):
    if f(s, 3 , 'e', '') and not f(s, 1 , 'e', ''):
        print(s)