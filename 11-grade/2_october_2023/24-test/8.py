def countSum(n):
    nOut = 0
    for s in n:
        nOut += int(s)
    return nOut


for n in range(1024):
    n2 = bin(n)[2::]
    n2 += str(countSum(n2) % 2)
    n2 += str(countSum(n2) % 2)

    if int(n2, 2) > 123:
        print(int(n2, 2))
        break