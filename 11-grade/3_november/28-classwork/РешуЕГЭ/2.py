from itertools import product

i = 0

for word in product('АВОРТ', repeat = 4):
    i+=1
    if ''.join(word) == 'ВАТА':
        print(i)