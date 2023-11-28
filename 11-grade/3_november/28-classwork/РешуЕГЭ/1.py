from itertools import product

i = 0

for word in product('АВСХ', repeat = 5):
    if (word[0] == 'Х' and word.count('Х') == 1) or word.count('Х') == 0:
        i+=1

print(i)
