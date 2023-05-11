num = 49 ** 10 + 7 ** 30 - 49
out = ''
while num > 0:
    out = str(num % 7) + out
    num //= 7

print(out.count('6'), out)