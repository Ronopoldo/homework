def f(x, A):
    return ((90 % A) == 0) and (((x % A) != 0) <= (((x % 15) == 0) <= ((x % 20) != 0)))

for A in range(1, 256):
    i = 0
    for x in range(1, 256):
        if f(x, A):
            i+=1
            # print('ae')
    if i == 255:
        print(A)