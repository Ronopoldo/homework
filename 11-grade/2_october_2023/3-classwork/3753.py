def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


def chetDiv(x):
    d = 0
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if i % 2 == 0:
                d += 1
            if (x // i) % 2 == 0:
                d += 1
        if d > 3:
            i = 74283943789
            break
    return d == 3


for n in range(113000000, 114000000 + 1):
    if chetDiv(n):
        print(n, div(n)[2])
