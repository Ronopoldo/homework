from itertools import product

lenOfWord = 8
counter = 0
arrange = product('CONST', repeat = lenOfWord)
arrange1 = product('CONST', repeat = lenOfWord)

begC = []
begO = []
begN = []
begSC = []
begSO = []
begSN = []
begST = []
begT = []

endC = []
endO = []
endN = []
endSC = []
endSO = []
endSN = []
endST = []
endT = []

for wordTup in arrange:
    word = ''.join(wordTup)
    wordOrigin = word
    if word[0] != 'S' and not 'SS' in word:
        word = word.replace('S','')
        if not(('CC' in word) or ('OO' in word) or ('NN' in word) or ('TT' in word)):
            if wordOrigin[lenOfWord-1] != 'S':
                eval('beg' + wordOrigin[lenOfWord-1] + '.append(wordOrigin)')
            else:
                eval('begS' + wordOrigin[lenOfWord - 2] + '.append(wordOrigin)')


for wordTup in arrange1:
    word = ''.join(wordTup)
    wordOrigin = word
    # print(wordOrigin)
    if word[lenOfWord-1] != 'S' and not 'SS' in word:
        word = word.replace('S','')
        if not(('CC' in word) or ('OO' in word) or ('NN' in word) or ('TT' in word)):
            if wordOrigin[0] != 'S':
                eval('end' + wordOrigin[0] + '.append(wordOrigin)')
            else:
                eval('endS' + wordOrigin[1] + '.append(wordOrigin)')

print(len(str(begC[123]) + str(endO[123])))
# print(begS)

print(f'S   {len(begSC) + len(begSO) + len(begSN) + len(begST)}   {len(endSC) + len(endSO) + len(endSN) + len(endST)}')
print(f'-Cs   {len(begSC)}   {len(endSC)}')
print(f'-Os   {len(begSO)}   {len(endSO)}')
print(f'-Ns   {len(begSN)}   {len(endSN)}')
print(f'-Ts   {len(begST)}   {len(endST)}')
print(f'C   {len(begC)}   {len(endC)}')
print(f'O   {len(begO)}   {len(endO)}')
print(f'N   {len(begN)}   {len(endN)}')
print(f'T   {len(begT)}   {len(endT)}')


forS = len(begSC) * len(endC) * 3 * 4 # Мы можем выполнить умножение на 3, т.к значения -Cs, -Os, -Ns, -Ts одинаковые; мы можем выполнить умножение на 4, т.к значения C, O, N, T одинаковые.
forOthers = (len(begC) * (len(endSO) + len(endSN) + len(endST)) + len(begC) * len(endO) * 3) * 4 # Мы можем выполнить умножение на 3 и умножение на 4, т.к элементы C, O, N, T и подзначения S повторяются.

print(forS, forOthers)

print(forS + forOthers)
# doubleArr = [][]
# print(len(end))

# print(counter) # 47088