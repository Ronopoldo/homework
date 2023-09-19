def f(s1, s2,c,m):
    if (s1+s2 >= 88): return c % 2 == m % 2
    if c == m: return 0
    h = [f(s1+1,s2, c + 1, m), f(s1*3,s2, c + 1, m), f(s1,s2+1, c + 1, m), f(s1,s2*3, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)

out = ''
for s1 in range(1, 72):
    for m in range(1,5):
        if f(6,s1,0, m) == 1:
            print(s1,m)
            if m == 3:
                out = out + str(s1)

print(out)

# 10
# 9232628
# 27