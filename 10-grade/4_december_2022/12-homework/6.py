from itertools import product

i = 0
arrange = product('ОЛЬГА', repeat = 5)
for word in arrange:
    if word.count('О') == 1 and word.count('Л') == 1 and word.count('Ь') == 1 and word.count('Г') == 1 and word.count('А') == 1:
        if word[0] != 'Ь' and word[word.index('Ь') - 1] not in ['О', 'А']:
            i+=1

print(i)