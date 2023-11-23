for N in range(100, 1000):
    sN = str(N)
    temp = [int(sN[0]) + int(sN[1]), int(sN[1]) + int(sN[2])]
    # print(temp)
    if sN[0] > sN[1]:
        out = str(temp[0]) + str(temp[1])
    else:
        out = str(temp[1]) + str(temp[0])

    if out == '1711':
        print(f'GOTCHA! {N}')

# 298 -> 11 17 -> 17 11 -> 1711