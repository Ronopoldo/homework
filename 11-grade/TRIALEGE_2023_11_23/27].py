
s = open('27.txt').read().split('\n')


newArray = []
for element in s:
    newArray.append(list(map(int,[element.split('  ')[0], element.split('  ')[1]])))
answerArray = []

print(newArray)

for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                for x5 in range(2):
                    for x6 in range(2):
                        for x7 in range(2):
                            for x8 in range(2):
                                for x9 in range(2):
                                    for x10 in range(2):
                                        for x11 in range(2):
                                            for x12 in range(2):
                                                for x13 in range(2):
                                                    for x14 in range(2):
                                                        for x15 in range(2):
                                                            for x16 in range(2):
                                                                for x17 in range(2):
                                                                    for x18 in range(2):
                                                                        for x19 in range(2):
                                                                            for x20 in range(2):
                                                                                sum = newArray[0][x1] + newArray[1][x2] + newArray[2][x3] + newArray[3][x4] + newArray[4][x5] + newArray[5][x6] + newArray[6][x7] + newArray[7][x8] + newArray[8][x9] + newArray[9][x10] + newArray[10][x11] + newArray[11][x12] + newArray[12][x13] + newArray[13][x14] + newArray[14][x15] + newArray[15][x16] + newArray[16][x17] + newArray[17][x18] + newArray[18][x19] + newArray[19][x20]
                                                                                if sum % 3 == 0:
                                                                                    answerArray.append(sum)

# 127026

print(max(answerArray))