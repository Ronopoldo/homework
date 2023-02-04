from itertools import product

arrange = product('ЗИМА', repeat = 5)
i = 0
for word in arrange:
    if ((word[0] == 'З' or word[0] == 'М') and (word[4] == 'И' or word[4] == 'А')):
        i = i + 1
        print(word)


print(i)

#256 (ПРОВЕРЕНО ВРУЧНУЮ)