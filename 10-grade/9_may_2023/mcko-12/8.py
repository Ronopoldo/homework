
p = 3
q = 5
e = 7

def f(n):
    return (p-1) * (q-1)



for d in range(65536):
    if (d * e) % f(1) == 1 and d < 40:
        print(d)