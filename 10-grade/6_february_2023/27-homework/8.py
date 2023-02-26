# from itertools import product
#
# arrange = product('СВЕТЛАН', repeat = 8)
#
# counter = 0
#
# for word in arrange:
#     if ((word.count('С') == 1) and (word.count('В') == 1) and (word.count('Е') == 1) and (word.count('Т') == 1) and (word.count('Л') == 1) and (word.count('А') == 2) and (word.count('Н') == 1)):
#         if ((word[word.index('А') - 1] != 'А') and (word[word.index('А') + 1] != 'А')):
#             counter+=1
#             print(word)
#
#
# print(counter)
#
#
# #57600




from itertools import product

arrange = product('СВЕТЛАН', repeat = 8)
i = 0

for word in arrange:
    if word.count('С') == 1 and word.count('В') == 1 and word.count('Е') == 1 and word.count('Т') == 1 and word.count('Л') == 1 and word.count('Н') == 1:
        temp = word.index('А')
        if ((word[temp - 1] != word[temp]) and (word[temp+1] != word[temp])) or ((word[0] == 'А' and word[1] != 'А')) or ((word[7] == 'А' and word[6] != 'А')):
            i+=1
            print(word)

print(i)

# 15120 (ПРОВЕРЕНО)