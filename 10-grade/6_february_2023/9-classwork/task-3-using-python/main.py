f = open('task.txt', 'r')
text = f.read().split('\n')
textLangs = ''

bigObj = {}

for i in range(0, 238):
    bigObj[text[i]] = 0
    # bigObj[text] = bigObj[text] + 1
for i in range(0, 238):
    bigObj[text[i]] = bigObj[text[i]] + 1


print(bigObj)
sorted_values = sorted(bigObj.values())
sorted_dict = {}

for i in sorted_values:
    for k in bigObj.keys():
        if bigObj[k] == i:
            sorted_dict[k] = bigObj[k]


print(sorted_dict)

more2langs = {'AFG': 2, 'ANT': 2, 'ASM': 2, 'BDI': 2, 'BLR': 2, 'CAN': 2, 'CYP': 2, 'FIN': 2, 'FRO': 2, 'GRL': 2, 'GUM': 2, 'IRL': 2, 'ISR': 2, 'KGZ': 2, 'LKA': 2, 'LSO': 2, 'MDG': 2, 'MHL': 2, 'MLT': 2, 'NRU': 2, 'PLW': 2, 'PRY': 2, 'ROM': 2, 'RWA': 2, 'SOM': 2, 'SYC': 2, 'TGO': 2, 'TON': 2, 'TUV': 2, 'WSM': 2, 'BEL': 3, 'BOL': 3, 'LUX': 3, 'PER': 3, 'SGP': 3, 'VUT': 3, 'CHE': 4, 'ZAF': 4}

f1 = open('task1.txt', 'r')
text1 = f1.read().split('\n')

final = {}
i = 0

for i in range(0, len(more2langs)):
    final[list(more2langs)[i]] = text1[i].split('*')[1]

print('final', final)


#
i = 0
answerObj = {}

for i in range(0, len(final)):
    answerObj[text1[i].split('*')[1]] = 0


for i in range(0, len(final)):
    answerObj[text1[i].split('*')[1]] = answerObj[text1[i].split('*')[1]] + 1

print(answerObj)

sorted_values = sorted(answerObj.values())
sorted_dict = {}

for i in sorted_values:
    for k in answerObj.keys():
        if answerObj[k] == i:
            sorted_dict[k] = answerObj[k]

print(sorted_dict)
