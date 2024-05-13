def f(x, A):
    return ((x & 45 > 0) or (x & 89 > 0)) <= (x & A > 0)

for A in range(256):
    for x in range(256):
        if f(x, A) == 0:
            break
    else:
        print(x, A)