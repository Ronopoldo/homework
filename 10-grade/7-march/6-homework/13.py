num = 5 ** 36 + 5 ** 24 - 25
out = ''

while num > 0:
    ost = num % 5
    out = str(ost) + out
    num //= 5

print(out.count('4'), out)

#22 (ПРОВЕРЕНО)