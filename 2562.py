def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


doubleArray = []

for n in range(174457, 174505 + 1):
    if len(div(n)) - 2 == 2:
        doubleArray.append([div(n)[1] * div(n)[2], (div(n)[1], div(n)[2])])

doubleArray = sorted(doubleArray)
for f in doubleArray:
    print(f[1])
