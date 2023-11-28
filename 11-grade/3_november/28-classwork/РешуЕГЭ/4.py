from itertools import product
i = 0
for word in product('АНДРЕЙ', repeat = 7):
    if word.count('А') == 1 and word.count('Й') == 1 and word[0] != 'Й':
        i+=1

print(i)