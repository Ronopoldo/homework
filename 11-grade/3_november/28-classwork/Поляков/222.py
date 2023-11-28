from itertools import product

activator = False
i=0

for tupleArray in product('АЗНС', repeat = 5):
    word = ''.join(tupleArray)
    if word == 'ЗАНАС':
        activator = True

    if activator == True:
        i+=1
        print(word)

    if word == 'САЗАН':
        activator = False

print(i)