def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for n in range(11275, 16328 + 1):
    if len(div(n)) == 5:
        print(div(n)[-3], div(n)[-2])
