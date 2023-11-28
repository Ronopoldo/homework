from itertools import product

i = 0
counter = 0

for word in product('АЕПСТУХ', repeat  = 4):
    i +=1
    if i > 1000:
        if 'АА' not in word and 'ЕЕ' not in word and 'ПП' not in word and 'СС' not in word and 'ТТ' not in word and 'УУ' not in word and 'ХХ':
            counter+=1

print(counter)