def f(s, e):
    if s > e or s == 11: return 0
    if s == e: return 1
    if s < e: return f(s + 1, e) + f(s * 2, e) + f(s ** 2, e)

print(f(2, 20))