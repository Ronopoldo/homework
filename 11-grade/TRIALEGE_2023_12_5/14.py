num = 25 ** 6 + 5 ** 18 - 5
ost = ''

while num > 0:
    ost = str(num % 5) + ost
    num //= 5

print(ost, ost.count('4'))

print(int('1000000444444444440', 5))