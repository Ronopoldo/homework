for n in range(9999,0, -1):
    n2 = bin(n)[2::]
    if (n % 2) == 0:
        n2+='00'
    else:
        n2+='11'
    if int(n2,2) < 94:
        print(int(n2, 2), n2, n)
        break