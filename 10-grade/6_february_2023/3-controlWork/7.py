from itertools import product

arrange = product('АВЕИЛРЯ', repeat = 3)

i = 0
for word in arrange:
    if (word.count('В') == 1):
        i = i + 1
        if (word.count('А') == 0):
            print(i, word)
            break

# 20 (ПРОВЕРИТЬ)

# ЗАБИЛ ХЫДЫДДЫДЫДДЫДЫЫДЫДДЫДЫДЫДЫДДЫддд