for i in range(9999):
    num = str(bin(i)[2::])
    if (i % 2 == 0):
        num = num + '01'
    else:
        num = num + '10'

    if (int(num, 2) > 102):
        print(int(num, 2))
        break


#105