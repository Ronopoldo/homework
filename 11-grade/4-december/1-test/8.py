from itertools import product
i = 0

for combo in product('0246*', repeat = 12):
    num = ''.join(combo)
    if num.count('*') == 5 and '**' not in num and num[0] != '0':
        i+=1
        print(num)


print(i * 4 ** 5)