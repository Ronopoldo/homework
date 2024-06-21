from itertools import product

nechet = '1357'

i =0

for combo in product('01234567', repeat=5):
    word = ''.join(combo)
    if word[0] != '0':
        if word[0] not in nechet:
            if word[-1] not in '26':
                if word.count('7') <= 2:
                    i+=1

print(i)