def f(b, e):
    if b > e or b == 25: return 0
    if b == e: return 1
    if b < e: return f(b+1, e) + f(b * 2, e)

print(f(2,14) * f(14, 29))