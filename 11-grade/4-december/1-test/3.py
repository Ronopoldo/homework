from itertools import product

i = 0
for combination in product('АПРСУ', repeat = 5):
    i+=1
    word = ''.join(combination)
    if (word[0] == 'У' and 'АА' not in word):
        print(i, word)
        break