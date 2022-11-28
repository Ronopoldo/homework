from itertools import product

arrange = product('0123456789ABCDEF', repeat=6)
i = 0
for word in arrange:
    if (word[0] != '1') and (word[-2] == 'A') and (word[-1] == 'B') and (word[0] != '0'):
        i += 1
        print(i, word)



