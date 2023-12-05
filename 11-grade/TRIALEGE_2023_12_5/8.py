from itertools import product

i = 0

for combo in product('АНДРЕЙ', repeat = 7):
    word = ''.join(combo)

    if word[0] != 'Й' and (word.count('А') == 1) and (word.count('Й') == 1):
        i+=1
        print(word, word.count('А'), word.count('Й'))


print(i)