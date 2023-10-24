for n in range(10000, 100000):
    nStr = str(n)

    n1 = int(nStr[0]) + int(nStr[2]) + int(nStr[4])
    n2 = int(nStr[1]) + int(nStr[3])
    if n1 > n2:
        Nout = str(n2) + str(n1)
    else:
        Nout = str(n1) + str(n2)
    if Nout == '723':
        print(n)
        break