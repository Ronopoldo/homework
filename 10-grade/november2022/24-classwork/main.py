from itertools import product
comb = product('СЛОН', repeat = 5)
amount = 0
for i in comb:
    word = ''.join(i)
    if (word.count('С') == 1):
        amount += 1

print(amount)
