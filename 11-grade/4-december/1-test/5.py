from itertools import product

sogl = 'СТВ'
gl = 'ЕО'
i = 0

for combo in product('ЕСТВО', repeat = 8):
    word = ''.join(combo)
    soglCount = word.count('С') + word.count('Т') + word.count('В')
    glCount = word.count('Е') + word.count('О')

    word = word.replace('Е', '*').replace('О', '*')

    if '**' not in word:
        if soglCount >= 4 and glCount >= 3:
            if 'ЕЕ' not in word and 'ОО' not in word and 'ЕО' not in word and 'ОЕ' not in word:
                i+=1
                print(combo, word, soglCount, glCount)



# ЕСООЕТЕЕ 4 6
# ЕСООЕТЕС 5 5
# 45360
print(i)

# 861443712
# 939524096
# 16777216