from itertools import permutations

i = 0

for word in permutations('БДНОРЫЯ'):
    i+=1
    if i == 3377:
        print(word)