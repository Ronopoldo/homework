def f(b, e):
    if b > e: return 0
    if b == e: return 1
    blist = list(str(b))
    if b < e and blist[len(blist) - 2] != 9: return f(b+1, e) + f(b + 10, e)
    if b < e and blist[len(blist) - 2] == 9: return f(b + 1, e)


print(f(12, 36))