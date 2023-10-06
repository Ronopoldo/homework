

def f(s, m):
    if s >= 30: return m % 2 == 0
    if m == 0: return 0
    h = [f(s+1, m-1), f(s*2, m-1)]
    return any(h) if (m-1) % 2 == 0 else any(h)

print('19)', [s for s in range(1, 30) if f(s, 3)])
print('20)', [s for s in range(1, 30) if not f(s, 1) or not f(s, 4)])
print('20)', [s for s in range(1, 30) if f(s, 5)])

# 4 1 2

