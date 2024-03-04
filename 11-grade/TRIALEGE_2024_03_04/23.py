def f(s, e):
    if s > e or s == 9: return 0
    if s == e: return 1
    if s < e: return f(s + 2, e) + f(s + 3, e) + f(s * 3, e)

print(f(3, 15) * f(15, 25))