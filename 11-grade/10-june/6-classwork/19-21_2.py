def f(s1, s2, s3, m):
    if (s1 >= 20) or (s2 >= 20) or (s3 >= 20) or ((s1 + s2 +s3) >= 25): return (m % 2) == 0
    if m == 0: return 0
    h = [
        f(s1*2,s2,s3,m-1),
        f(s1,s2*2,s3,m-1),
        f(s1,s2,s3*2,m-1),
        f(s1+2,s2+2,s3+2,m-1)
    ]

    if ((m - 1) % 2) != 0:
        return all(h)
    else:
        return any(h)



for s in range(1,19):
    if f(2,3,s, 4) and not f(2,3,s, 2):
        print(s)