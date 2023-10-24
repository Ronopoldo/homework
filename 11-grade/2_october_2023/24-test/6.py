for n in range(100, 1000):
    nstr = str(n)
    n1 = int(nstr[0]) + int(nstr[1])
    n2 = int(nstr[2]) + int(nstr[1])

    if n1 > n2:
        Nout = str(n2)+ str(n1)
    else:
        Nout = str(n1) + str(n2)


    if Nout == '812':
        print(n)
        break