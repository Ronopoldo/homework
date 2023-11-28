from itertools import product

i = 0
for word in product('АИМРЯ', repeat = 4):
    i+=1
    if i == 211:
        print(word)