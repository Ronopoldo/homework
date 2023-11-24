
from itertools import permutations
arrange = permutations('001122334455667788', 10)
counter = 0

for originNumber in arrange:
    num = ''.join(originNumber)
    if num[0] != '0':
        counter+=1
    print(num)
print(counter)