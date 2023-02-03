def f(n, m):
    return n % m == 0

for A in range(1, 8192):
    i = 0
    for x in range(1, 128):
        if ((f(A, 45) and (f(750,x)) <= ((not f(A,x)) <= (not f(120,x))))):
            i+=1
    if i == 127:
        print(A)

# 90