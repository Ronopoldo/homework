def f(x, A):
    return (x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))

for A in range(256):
    tmp = 0
    for x in range(256):
        if f(x,A):
            tmp+=1

    if tmp == 256:
        print(A)