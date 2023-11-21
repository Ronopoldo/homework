from itertools import *
arrange = permutations('ДОБРЫНЯ', 6)
gl = 'ОЫЯ'
forbidden = product(gl, repeat = 2)
forbiddenList = []
for key in forbidden:
    forbiddenList.append(''.join(key))
counter = 0
for word in arrange:
    iS = 0
    iG = 0
    forbidden = False
    for letter in gl:
        if letter in gl:
            iG+=1
    for key in forbiddenList:
        if key in ''.join(word):
            forbidden = True
    if (forbidden == False) and ((6 - iG) > iG):
        counter+=1
print(counter)