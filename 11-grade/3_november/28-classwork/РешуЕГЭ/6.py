from itertools import product
i = 0

for num in product('12345', repeat = 5):
    if num.count('1') == 3:
        i+=1

print(i)
