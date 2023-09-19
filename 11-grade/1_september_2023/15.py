def f(m,n):
    return m & n
for A in range(1024):
    counter = 0
    for x in range(256):
        if (f(x,51) == 0) or (f(x,41 == 0) <= (f(x,A) == 0)):
            counter+=1

    if counter == 256:
        print(A)