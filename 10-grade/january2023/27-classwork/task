keys = {
    '.,?:!': 1,
    'ABC': 2,
    'DEF': 3,
    'GHI': 4,
    'JKL': 5,
    'MNO': 6,
    'PQRS': 7,
    'TUV': 8,
    'WXYZ': 9,
    ' ': 10
}
answer = ''

word = (str(input())).upper()
for i in range(0, len(word)):
    notDefined = True
    # print(i+1)
    k = -1
    while notDefined == True:
        k = k + 1
        if word[i] in list(keys)[k]:
            notDefined = False
            print(k)

    strType = list(keys)[k]
    addPart = (list(keys)[k].index(word[i]) + 1) * str(k + 1)
    answer = answer + addPart

print('ended')

print(answer)

