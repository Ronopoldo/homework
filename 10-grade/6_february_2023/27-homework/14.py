def f(m, n):
    return  m & n

for A in range(0,128):
    i = 0
    for x in range(0,1024):
        if ((f(x,25) != 0) <= ((f(x, 19) == 0) <= (f(x,A) != 0))):
            i+=1
    if i == 1024:
        print(A)

# 8 (ПРОВЕРЕНО)