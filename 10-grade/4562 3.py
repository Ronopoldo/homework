from itertools import product

lenOfWord = 5
counter = 0
arrange = product('CONST', repeat = lenOfWord)

for wordTup in arrange:
    word = ''.join(wordTup)
    wordOrigin = word
    if word[0] != 'S' and word[lenOfWord - 1] != 'S' and not 'SS' in word:
        word = word.replace('S','')
        if not(('CC' in word) or ('OO' in word) or ('NN' in word) or ('SS' in word) or ('TT' in word)):
            counter+=1

print(counter)