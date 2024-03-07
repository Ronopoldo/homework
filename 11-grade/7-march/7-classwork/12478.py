# 100000 1000 18000

begin = 1000
end = 18000

s = open('12478.txt').read().split('\n')

origin = []

for ele in s:
    origin.append([int(ele.split(' ')[1]) - begin, int(ele.split(' ')[0]) - begin])

print(sorted(origin,reverse=True))

tempoEnd = 18000
neededEle=[]
tempMin = 65536
prev = 1234678
i = 0

while tempoEnd >= 1000:
    lastN = 65536
    for ele in origin:
        if ele[0] > tempoEnd:
            tempMin = min(tempMin, ele[1])
            neededEle = ele
    prev = tempoEnd
    tempoEnd = tempMin
    i+=1

answer2 = []

tempMax = 0
for ele in origin:
    if ele[0] > prev:
        if (tempMax < ele[0]) and (ele[1] <= 1000):
            answer2 = ele
            tempMax = ele[0]


print(i, answer2[0] - answer2[1], prev)









'''
# 100000 1000 18000

begin = 1000
end = 18000

s = open('12478.txt').read().split('\n')

origin = []

for ele in s:
    origin.append([int(ele.split(' ')[1]) - begin, int(ele.split(' ')[0]) - begin])

print(sorted(origin,reverse=True))

tempoEnd = 18000
tempMin = 65536
i = 0

while tempoEnd >= 1000:
    lastN = 65536
    for ele in origin:
        if ele[0] > tempoEnd:
            tempMin = min(tempMin, ele[1])

    tempoEnd = tempMin
    i+=1

print(i, )
'''




