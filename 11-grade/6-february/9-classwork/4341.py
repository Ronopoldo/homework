def f(s, m):
    if s >= 125:
        if s < 163: return m % 2 == 0
        else: return m % 2 != 0
    if m == 0: return 0
    hp = [f(s+2, m-1), f(s+4, m-1), f(s*2, m-1)]
    hv = [f(s+2, m-1), f(s+4, m-1)]
    return any(hp) if (m-1) % 2 == 0 else all(hp)

print('19)', [s for s in range(1, 125) if f(s, 2)])
print('20)', [s for s in range(1, 125) if f(s, 3) and not f(s, 1)])
print('21)', [s for s in range(1, 125) if f(s, 4)and not f(s, 2)])