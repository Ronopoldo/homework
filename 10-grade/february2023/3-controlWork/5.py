for N1 in range(10000, 1000, -1):
    N = str(N1)
    summs = [int(N[0]) + int(N[1]), int(N[1]) + int(N[2]), int(N[2]) + int(N[3])]
    summs.remove(min(summs))
    newN = sorted(summs)
    finalN = str(newN[0]) + str(newN[1])
    if finalN == '613':
        print(N1)
        break
# 9424
# 13; 6; 6
# 6 + 13
# 613