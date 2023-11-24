
from itertools import permutations
arrange = permutations('0123456789ABCDEF', 3)
counter = 0
for originNumber in arrange:
    num = ''.join(originNumber)
    for i in range(0,10,2):
        num = num.replace(str(i), '*')
    for i in range(1, 10, 2):
        num = num.replace(str(i), '#')

    num = num.replace('A', '*').replace('C', '*').replace('E', '*')
    num = num.replace('B', '#').replace('D', '#').replace('F', '#')

    if (''.join(originNumber)[0] != '0') and ('**' not in num) and ('##' not in num):
        counter+=1
print(counter)