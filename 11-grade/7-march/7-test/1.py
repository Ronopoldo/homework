def f(s, m):
    if s >= 50: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s + 3, m - 1),
        f(s * 2, m -1)
    ]

    if (m - 1) % 2 == 0:
        return any(h)
    else:
        return all(h)


for s in range(50):
    if f(s, 4) and not f(s, 2):
        print(s)

# 19) 22
# 20) 11_21
# 21) 18

'''
1. 22; 11_21; 18 (V)
2. 13; 4; 8_9 (V(x))
3. 34; 1; 11_32 (V)
'''

