# 128 6288 33
# 7 20 2
# Кол-во домов; длина дороги; дельта почтамта
# Дом ; кол-во писем
length = 20
capacity = 20
delta = 2

s = open('test.txt').read().split('\n')
homes = []
for ele in s:
    homes.append([int(ele.split(' ')[0]), int(ele.split(' ')[1])])
homes.sort()

houseMap = []
for ele in homes:
    houseMap.append(ele[0])

map = [0] * length

for i in range(len(map)):
    if i in houseMap:
        map[i] = homes[houseMap.index(i)][1]

houseMap.append(435)
print(map)
print(houseMap)
print(homes)


def sumOfArr(inp):
    output = 0
    for ele in inp:
        output += int(ele)
    return output


def mailsForHouse(delta, amount):
    i = 0
    while amount >= 20:
        amount -= 20
        i += 1
    if amount > 0:
        i += 1

    return (delta) * (i)


totals = []

for post in range(length):
    if post >= delta:
        arrange = map[post - delta:1 + post + delta]
    else:
        arrange = map[length - (delta - post):length] + (map[0:(delta - map[post + delta])])
    print(sumOfArr(arrange) == 0, post, arrange, len(arrange))

    if sumOfArr(arrange) == 0:
        total = 0
        for i in range(len(map)):
            total += mailsForHouse(min(abs(post - i), length - abs(post - i)) + 1, map[i])
            # total+=mailsForHouse(abs(post - i), abs())
        # 738658
        #     print(post)
        totals.append(total)

print(sorted(totals))
print(min(totals), totals.index(min(totals)))

# print( totals.index(738658))
