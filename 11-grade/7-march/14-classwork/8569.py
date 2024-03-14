# 12000 - кол-во машин
# 75 - кол-во мест на этаж
# 125 - стоимость этажа 1
# 3 уровня


s = open('8569.txt').read().split('\n')
sNew = []

for ele in range(len(s)):
    sNew += ['']
    sNew[ele] = [int((s[ele].split(' '))[0]), int((s[ele].split(' '))[1]), int((s[ele].split(' '))[2])]

sNew = sorted(sNew)

lvl1 = [0 for i in range(75)]
lvl2 = [0 for i in range(75)]
lvl3 = [0 for i in range(75)]

print(sNew)

client = 0
income = 0
loser = 0

for time in range(72_000):

    for car in range(len(lvl1)):
        if time == lvl1[car]:
            lvl1[car] = 0

    for car in range(len(lvl2)):
        if time == lvl2[car]:
            lvl2[car] = 0

    for car in range(len(lvl3)):
        if time == lvl3[car]:
            lvl3[car] = 0

    for ele in sNew:
        if ele[0] == time:
            if (0 in lvl1) and (ele[2] == 1):
                income += ((ele[1] - ele[0]) / 60 // 60 + 1)*125
                lvl1[lvl1.index(0)] = ele[1] + 60
                client += 1

            elif 0 in lvl2 and (ele[2] == 2):
                income += ((ele[1] - ele[0]) / 60 // 60 + 1)*125 * 2
                lvl2[lvl2.index(0)] = ele[1] + 60
                client += 1

            elif 0 in lvl3 and (ele[2] == 3):
                income += ((ele[1] - ele[0]) / 60 // 60 + 1) *125 * 4
                lvl3[lvl3.index(0)] = ele[1] + 60
                client += 1
            else:
                loser += 1

    print(income, client, loser, time)

print(int(income), client)

# 1528625 647
'''
                if ((ele[1] - ele[0]) / 60 // 60) != int((ele[1] - ele[0]) / 60 / 60):
                    income += ((ele[1] - ele[0]) / 60 // 60 + 1) *125 * 4
                else:
                    income += ((ele[1] - ele[0]) / 60 // 60) * 125 * 4
'''