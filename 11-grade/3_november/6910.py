from itertools import permutations
arrange = permutations('ABCDEF', 4)
counter = 0
for originNumber in arrange:
    num = ''.join(originNumber)
    num = num.replace('A', '$').replace('B', '$').replace('D', '$').replace('E', '$')
    if ('$$' not in originNumber):
        counter+=1
print(counter)