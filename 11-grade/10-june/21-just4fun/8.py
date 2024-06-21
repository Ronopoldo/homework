from itertools import product

nechet = '1357'

i =0

# Нечётная НЕ рядом с 4

blackList = ['14','34','54','74','41','43','45','47']

for combo in product('01234567', repeat=5):
    word = ''.join(combo)
    if word[0] != '0':
        tmp = True
        for ele in blackList:
            if ele in word:
                tmp = False
        if (tmp == True) and (word.count('4') == 1):
            i+=1

print(i)