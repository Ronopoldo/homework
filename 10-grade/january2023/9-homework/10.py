num = 9 ** 8 + 3 ** 8 - 2
res = ''

while num > 0:
    ost = num % 3
    num = num // 3
    res = str(ost) + res

print(res, res.count('2'))

#7