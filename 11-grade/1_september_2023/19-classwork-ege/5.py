for n in range(2000):
    n2 = bin(n)[2::]
    if int(n2) % 2 == 0:
        n2 = n2 + '00'
    else:
        n2 = n2 + '11'

    if int(n2, 2) < 94:
        print(n)

# 22 - проверено