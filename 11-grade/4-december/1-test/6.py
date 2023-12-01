from itertools import permutations

chet = '0246'
nechet = '1357'

i = 0

for combo in permutations('01234567'):
    num = ''.join(combo)
    if num[0] != '0':
        num = num.replace('0', '*').replace('2', '*').replace('4', '*').replace('6', '*')
        num = num.replace('1', '#').replace('3', '#').replace('5', '#').replace('7', '#')

        if '##' not in num and '**' not in num:
            i+=1
            print(combo, num)


print(i)