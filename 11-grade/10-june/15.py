B = [i for i in range(50, 71)]

print(B)

def f(x, A):
    return ((x % A) == 0) or ((x in B) <= (not (x % 21) == 0))

for A in range(4096, 0, -1):
    i = 0
    for x in range(256):
        if f(x, A):
            i+=1
    if i == 256:
        print(A)