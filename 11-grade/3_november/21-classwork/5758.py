from itertools import *

arrange = product('АНТИУОПЯ', repeat = 6)


gl = 'АИУОЯ'
sogl = 'НТП'
def f(insert, index):
    finalWord = ''
    finalWord2 = ''
    for l in range(index):
        finalWord+=insert[l]
    for l in range(index, len(insert)):
        finalWord2+=insert[l]
    return [finalWord, finalWord2]


print(f('ABCDE', 3))

i = 0
print(sorted('BADCE', reverse=True))
for s in arrange:
    word = ''.join(s)
    for key in range(2,6):
        print(word)
        print(f(word, key))
        if (sorted(f(word, key)[0], reverse=True) == list(f(word, key)[0])) and (sorted(f(word, key)[1]) == list(f(word, key)[1])):
            gli = 0
            sogli = 0
            for letter in f(word, key)[0]:
                if letter in gl:
                    gli+=1
            for letter in f(word, key)[1]:
                if letter not in gl:
                    sogli+=1

            if sogli == len(f(word, key)[1]) and gli == len(f(word, key)[1]):
                i+=1
print(i)

#1478