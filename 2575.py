def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for n in range(int(244143 ** 0.25), int(1367821 ** 0.25) + 1):
    if len(div(n)) == 2:
        print(n ** 2, n ** 3)

print('doned')
