from itertools import product

arrange = product('01234567', repeat = 5)
notChet = ['1', '3', '5', '7']
i = 0

for num in arrange:
    if num.count('6') == 1 and num[0] != '0':
        if num.index('6') == 4:
            if (num[(num.index('6') - 1)] not in notChet):
                i = i + 1
                print(num)
        elif num.index('6') == 0:
            if (num[(num.index('6') + 1)] not in notChet):
                i = i + 1
                print(num)
        else:
            if (num[(num.index('6') - 1)] not in notChet) and (num[(num.index('6') + 1)] not in notChet):
                i = i + 1
                print(num)

print(i)

#2961