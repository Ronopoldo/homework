def f(x, A):
    return ((x&57 > 0) or  (x&99 > 0)) <= (x&A > 0)


for A in range(0, 256):
    i = 0
    for x in range(0, 256):
        if f(x, A):
            i+=1
    if i == 256:
        print(A)