from itertools import permutations

arrange = permutations('ПАРАБОЛА')
i = 0

for word in arrange:
    sWord = ''.join(word)

    sWord = sWord.replace('А', '*').replace('О', '*')
    sWord = sWord.replace('П', '#').replace('Р', '#').replace('Б', '#').replace('Л', '#')
    if ('**##' not in sWord) and ('##**' not in sWord):
        i+=1
        print(sWord, word)
print(i)