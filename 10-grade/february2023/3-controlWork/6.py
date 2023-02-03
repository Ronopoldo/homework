from itertools import product

arrange = product('ВИШНЯ', repeat = 6)
glas = ['И', 'Я']
i = 0

for word in arrange:
    if (word.count('В') == 1 and (word[0] != 'Ш') and (word[5] not in glas)):
        i = i + 1
        print(word, word.count('В'))


print(i)

# 2816