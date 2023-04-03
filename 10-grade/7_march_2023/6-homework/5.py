for N in range(10000,100000):
    N1 = int(str(N)[0]) + int(str(N)[2]) + int(str(N)[4])
    N2 = int(str(N)[1]) + int(str(N)[3])

    if N1 < N2:
        new = (str(N1) + str(N2))
    else:
        new = (str(N2) + str(N1))

    if new == '621':
        print(N)


# 30969 (ПРОВЕРЕНО)