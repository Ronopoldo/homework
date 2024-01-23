def summa(num):
    temp = 0
    for cur in str(num):
        temp+=int(cur)

    return temp


print()



for n in range(8192):
    n2 = bin(n)[2::]
    if summa(int(n2, 2)) % 2 == 0:
        n2+='0'
    else:
        n2+='1'

    if summa(int(n2, 2)) % 2 == 0:
        n2+='0'
    else:
        n2+='1'

    if summa(int(n2, 2)) % 2 == 0:
        n2+='0'
    else:
        n2+='1'

    R = int(n2, 2)

    if R > 2054:
        print(R, int(n2, 2), n)
        break