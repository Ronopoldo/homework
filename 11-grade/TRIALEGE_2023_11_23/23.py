def f(s, e):
    if s > e or s == 5 or s == 10: return 0
    if s == e: return 1
    if s < e: return f(s + 1, e) + f(s * 2, e) + f(s + 3, e)

print(f(2, 14))


