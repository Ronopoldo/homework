# СПОСОБ 1
from itertools import product

arrange = product('ГЕКЭ023', repeat=4)
i=0
for word in arrange:
    i += 1
    if (word[0] == '0') and (word[1] != word[2]) and (word[2] != word[3]) and (word[1] != word[0]):
        print(i, word)
        break








# СПОСОБ 2
alpha = 'ГЕКЭ023'
i = 0

for x1 in alpha:
    for x2 in alpha:
        for x3 in alpha:
            for x4 in alpha:
                sl = x1 + x2 + x3 + x4
                if sl[0] == '0' and sl[0] != sl[1] and sl[1] != sl[2] and sl[2] != sl[1] and sl[3] != sl[1]:
                    print(i, word)
                i += 1
