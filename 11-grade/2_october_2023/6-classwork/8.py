from itertools import product

arrange = product('ЕКМОПРТЬЮ', repeat = 5)

i = 0
for word in arrange:
    i+=1
    if word[0] != 'Ь' and word.count('К') == 2 and i % 2 != 0:
        print(i, word)


#58