def suma(num):
    out = 0
    numS = str(num)
    for let in numS:
        out+=int(let)
    return out




maxi = 0


for count5 in range(4, 10000):
    num = '3' + '5' * count5
    while ('333' in num) or ('555' in num):
        if '555' in num:
            num = num.replace('555', '3', 1)
        else:
            num = num.replace('333','5',1)

    maxi = max(maxi, suma(num))
    print(count5)


print(maxi)