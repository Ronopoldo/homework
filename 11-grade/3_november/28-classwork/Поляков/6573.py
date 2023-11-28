from itertools import product

sogl = 'ПСХ'
i = 0

for word in product('ЕПСУХ', repeat = 5):
    # print(''.join(word), word[-1])
    if ''.join(word)[-1] in sogl:
        i+=1
        if ''.join(word) == 'УСПЕХ':
            print(i)