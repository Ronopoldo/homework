def sumOfDigits(num):
    out = 0
    for digit in str(num):
        out+=int(digit)
    return out

for n in range(4, 1024):
    origin = '2' + '5' * n
    while ('25' in origin) or ('355' in origin) or ('555' in origin):
        if ('25' in origin):
            origin = origin.replace('25','5',1)
        if ('355' in origin):
            origin = origin.replace('355', '52', 1)
        if ('555' in origin):
            origin = origin.replace('555', '3', 1)


    if sumOfDigits(origin) == 17:
        print(n)
        break

    '''
    НАЧАЛО
ПОКА нашлось (25) ИЛИ нашлось (355) ИЛИ нашлось (555)
    ЕСЛИ нашлось (25)
        ТО заменить (25, 5)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (355)
        ТО заменить (355, 52)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (555)
        ТО заменить (555, 3)
    КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
'''