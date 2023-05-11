def f(b,e):
    if b > e: return 0
    if b == e: return 1
    if b < e: return f(b + 1, e) + f(b + 3, e)


print(f(17,30))