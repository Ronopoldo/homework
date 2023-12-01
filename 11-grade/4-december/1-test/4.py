from itertools import product
i = 0

sogl = 'КМПГ'
gl = 'ОЕЭ'

for combo in product('КОМПЕГЭ', repeat = 6):
    word = ''.join(combo)

    if word[0] in gl and word [1] in sogl and word[2] in sogl and word[3] in sogl and word[4] in sogl and word[5] in gl:
        i+=1


print(i)
