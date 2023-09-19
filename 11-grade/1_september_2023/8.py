from itertools import product

arrange = product('ВИШНЯ', repeat = 6)
counter = 0

for word in arrange:
    w = list(word)
    if (w.count('В') <= 1) and (w[0] != 'Ш') and (w[5] != 'И')  and (w[5] != 'Я'):
        print(word)
        counter+=1

print(counter)

# 4352