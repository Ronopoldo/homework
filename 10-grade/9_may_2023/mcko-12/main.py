for N in range(4096):
    N2 = str(bin(N)[2::])
    if N % 2 == 0:
        N2 = N2 + '00'
    else:
        N2 = N2 + '11'

    if N2.count('1') % 2 == 0:
        N2 = N2 + N2[-2]
    else:
        N2 = N2 + N2[-1]


    if int(N2,2) > 80:
        print(N)
        # break
        # exit

