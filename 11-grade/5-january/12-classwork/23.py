def f(s, e):
    if s > e or s == 16: return 0
    if s == e: return 1
    if s < e: return f(s + 1, e) + f(s + 3, e) + f(s ** 2, e)


print(f(3, 20) * f(20, 26))