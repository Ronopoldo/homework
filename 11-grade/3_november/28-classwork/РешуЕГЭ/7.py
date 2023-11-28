from itertools import product

i = 0
sogl = 'ЛТ'


for word in product('ЛЕТО', repeat = 4):
    if word[0] in sogl:
        i+=1

print(i)