def f(s, m):
    if s == 42: return m % 2 == 0
    if m == 0: return 0
    if s < 42:
        h = [f(s+1, m-1), f(s+3, m-1), f(s+7, m-1)]
    if s > 42:
        h = [f(s - 1, m - 1), f(s - 3, m - 1), f(s - 7, m - 1)]
    return any(h) if (m-1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 2048) if f(s, 2)])
print('20)', [s for s in range(1, 2048) if f(s, 3) and not f(s, 1)])
print('21)', [s for s in range(1, 2048) if f(s, 4) and not f(s, 2)])