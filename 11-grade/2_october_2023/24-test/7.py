for n in range(2048):

    n2 = bin(n)[2::]

    if n2.count('1') > n2.count('0'):
        n2 += '1'
    else:
        n2+='0'

    if int(n2, 2) > 100:
        print(int(n2, 2))
        break