# 500
# 24          8
# ВАГОНЫ  КУПЕ/ВАГОН


s = open('7356.txt').read().split('\n')

groups = []

# train = {}
#
#
# for i in range(1, 25):
#     train[i] = {'Купе': 8, 'Полукупе': 8}
#
# print(train)

kupe = 8 * 24
avialableKupe = 0
halfKupe = 8 * 24


'''
    {
        1: {
            купе: 0,
            пкупе: 8
        },
        3: {
            купе: 8,
            пкупе: 8
        },
        2: {
            купе: 8,
            пкупе: 8
        }
    }
    '''

for ele in s:
    groups.append([int(ele.split(' ')[0]), int(ele.split(' ')[1])])

groups = sorted(groups, reverse=True)
children = 0

freePlaces = [0 for i in range(24)]


currentGroupNum = 0
currentPairNum = 0

for group in groups:
    if (group[0] > 2) and (kupe > 0):
        kupe-=1
        children+=group[1]
        currentGroupNum += 1
        if (currentGroupNum // 8) < 24:
            freePlaces[currentGroupNum // 8] += (4 - group[0])

    if (group[0] <= 2) and (halfKupe > 0):
        halfKupe-=1
        children+=group[1]
        currentPairNum += 1
        if (currentPairNum // 8) < 24:
            freePlaces[currentPairNum // 8] += (2 - group[0])
    # print(children, max(freePlaces))
print(freePlaces)
print(children, freePlaces.index(max(freePlaces)) + 1)

# t = 0
# for ele in groups:
#     t+=ele[0]
#
# print(t, 24* ((8 * 4) + (8 * 2)))
# print(groups)
