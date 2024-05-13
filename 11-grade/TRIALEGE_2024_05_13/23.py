def f(s, e):
    if s > e: return 0
    if s == e: return 1
    if s < e: return f(s + 1, e) + f(s + 2, e) + f(s + 4, e)


print(f(21, 30))