n = 729 ** 6 - 3 ** 20 + 90

print(n)

ost = ''
while n > 0:
    ost = str(n % 9) + ost
    n//=9

print(ost, ost.count('0'))