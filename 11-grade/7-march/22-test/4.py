def deli(n, m):
    return (n % m) == 0

def f(x, A):
    return (A < 50) and ((not deli(x, A)) <= (deli(x, 10) <= (not deli(x, 18))))

for A in range(1, 256):
    i = 0
    for x in range(1, 256):
        if f(x, A):
            i+=1
    if i == 255:
        print(A)

