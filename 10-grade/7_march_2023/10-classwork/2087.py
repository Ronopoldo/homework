from itertools import permutations
s = ''
isFound = False

while s != '34':
    for amount in range(0, 32):
        arrange = permutations('1111111111' + '2' * amount)
        for num in arrange:
           # print(''.join(num), len(num), isFound)
            s = ''.join(num).replace('21', '5')

            output = []
            for i in range(len(list(s))):
                output.append(int(list(s)[i]))
            print(sum(output), isFound)
            if sum(output) == 34:
                print(amount, num)
                isFound = True
                break


print('done')