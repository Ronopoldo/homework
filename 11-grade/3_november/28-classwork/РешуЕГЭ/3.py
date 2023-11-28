from itertools import product

i = 0

for word in product('АОУ', repeat = 5):
    i+=1
    if ''.join(word) == 'ОАОАО':
        print(i)