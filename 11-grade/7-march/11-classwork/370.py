def DEL(m, n):
    return m % n == 0

def f(x, A):
    return (not DEL(x,A)) <= (DEL(x,6) <= (not DEL(x,4)))



for A in range(1, 65536):
    tmp = 0
    for x in range(256):
        if f(x,A):
            tmp+=1

    if tmp == 256:
        print(A)