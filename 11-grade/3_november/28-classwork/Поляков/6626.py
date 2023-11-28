from itertools import product

i = 0
counter = 0

for word in product('ЬРПЛЕА', repeat = 5):
    i +=1

    if i <= 387 and word[-1] == 'Ь':
        counter+=1

print(counter)