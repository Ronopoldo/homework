from itertools import product



for combo in product('0123456789ABCDEF', repeat = 15):
    num = ''.join(combo)
    if num[0] != '0':
        print(num. sorted(num))