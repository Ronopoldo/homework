from itertools import product

arrange = product('ABCDEX', repeat = 4)

counter = 0

for word in arrange:
    if word.count('X') == 1:
        counter+=1


print(counter)