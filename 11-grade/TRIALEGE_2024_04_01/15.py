def f(x, y, A):
    return ((y + 2 * x ) != 48) or (A < x) or (A < y)


for A in range(2048):
    i = 0
    for x in range(256):
        for y in range(256):
            if f(x,y, A):
                i+=1


    if i == 256**2:
        print(A)