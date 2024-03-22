def f(x, A):
    return (((x & 114) != 0) or ((x & 94) != 0)) <= (((x & 73) == 0) <= ((x & A) != 0))

for A in range(256):
    i = 0
    for x in range(256):
        if f(x, A):
            i+=1
    if i == 256:
        print(A)

