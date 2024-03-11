def corner(a,b,c):
    return a + b + c == 180


def f(x, A):
    return corner(37, A, x + 45) == corner(A, x, 90) and (not (A + 23 < 120))


for A in range(1, 256):
    tmp = 0
    for x in range(1, 256):
        if f(x,A):
            tmp+=1

    if tmp == 255:
        print(A)