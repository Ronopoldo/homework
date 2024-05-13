def countDels(inp):
    dls = []
    for i in range(1, inp + 1):
        if inp % i == 0:
            dls.append(i)

    return len(dls)

maxDels = -1

for i in range(568_023, 569231):
    maxDels = max(maxDels, countDels(i))
    print(i)

for i in range(568_023, 569231):
    if countDels(i) == maxDels:
        print(countDels(i), i, maxDels)