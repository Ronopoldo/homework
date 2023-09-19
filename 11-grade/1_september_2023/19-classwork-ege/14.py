num = 3 * 343 ** 8 + 5 * 49 ** 12 + 7 ** 15 - 49
ost = ''
while num > 0:
    ost = str(num % 7) + ost
    num //= 7

print(ost)
print(ost.count('6'))
print(ost.count('0'))