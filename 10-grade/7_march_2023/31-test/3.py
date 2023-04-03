num = '1' * 50 + '2' * 50 + '3' * 50

while ('12' in num or '32' in num or '31' in num):
    if '12' in num:
        num = num.replace('12', '21', 1)
    if '32' in num:
        num = num.replace('32', '23', 1)
    if '31' in num:
        num = num.replace('31', '13', 1)

print(list(num)[19] + list(num)[79] + list(num)[119])
