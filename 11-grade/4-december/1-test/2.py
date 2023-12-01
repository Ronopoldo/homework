from itertools import product
i = 0
for word in product('АГНРТ', repeat=6):
    i +=1
    if ''.join(word) == 'ГРАНАТ':
        print(i)