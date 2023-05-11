from itertools import product

arrange = product('АВОРТ', repeat = 4)
i = 1
for word in arrange:

    if ''.join(word) == 'ВАТА':
        print(i)
    i += 1