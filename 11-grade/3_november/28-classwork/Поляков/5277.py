from itertools import permutations

i = 0
out = []

for word in permutations('АИКЛМЬ'):
    out.append(''.join(word))

print(out)

for w in out:
    if w[0] == 'К' and w[-1] == 'Ь':
        if out.index(w) - out.index(w[::-1]) == 26655 or out.index(w[::-1]) - out.index(w) == 26655:
            print('ae')
            print(out.index(w))