from itertools import permutations
s = ''
isFound = True

for amount in range(1,10):

        s = '21' * amount + '1' * (20 - len('21'*amount))

        print(s)
        print(s.replace('21','5'))

        print(int(s.replace('21','5')))
        print()




print('done')