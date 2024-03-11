def f(x,y, A):
    return (4 * x + y > 115) or (x > 3*y) or (x + 4*y < A)


for A in range(-1024, 1024):
    tmp = 0
    for x in range(128):
        for y in range(128):
            if f(x,y,A) == False:
                tmp+=1

    if tmp >= 1:
        print(A)