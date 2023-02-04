from itertools import product
arrange = product('ABCDX', repeat = 4)
i = 0

for word in arrange:
    if (word.count('X') == 1):
        i+=1

print(i)