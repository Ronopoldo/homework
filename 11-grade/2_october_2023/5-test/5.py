counter = 0
for n in range(1000, 10000):
    sn = str(n)
    if (int(sn[0]) % 2 != 0) and (int(sn[1]) % 2 != 0) and (int(sn[2]) % 2 != 0) and (int(sn[3]) % 2 != 0):
        sum1 = str(int(sn[0]) + int(sn[1]))
        sum2 = str(int(sn[2]) + int(sn[3]))
        if int(sum1) < int(sum2):
            out = sum1 + sum2
        else:
            out = sum2 + sum1

        if out == '616':
            counter+=1


print(counter)


