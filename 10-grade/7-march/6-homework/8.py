from itertools import product
arrange = product('АВСХ', repeat = 5)

i = 0
for word in arrange:
    if (word[0] != 'Х') and (word[1] != 'Х') and (word[2] != 'Х') and (word[3] != 'Х'):
        i+=1

print(i)

'''
324 (ПРОВЕРЕНО РУЧНЫМ СПОСОБОМ И СИСТЕМОЙ)

Ручная проверка:
3 * 3 * 3 * 3 * (*)
* = 4

3^4*4=324


'''