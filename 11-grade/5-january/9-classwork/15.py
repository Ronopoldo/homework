def f(x, a):
    return (x & a == 0) or not(x & 37 == 0) or not(x & 12 == 0)


for A in range(1, 1024):
    flag = True
    for x in range(1, 512):
        if f(x,A) == False:
            flag = False

    