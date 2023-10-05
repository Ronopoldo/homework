def f(s, e):
    if s > e: return 0
    if s == e: return 1
    if s < e: return f(s + 1, e) + f(s + 3, e)
print(f(1, 8) * f(8, 15))

