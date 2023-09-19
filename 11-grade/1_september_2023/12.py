num = '0' + '1' * 12 + '2' * 15 + '3' * 17
while '01' in num or '02' in num or '03' in num:
    num = num.replace('01', '20')
    num = num.replace('02', '120')
    num = num.replace('03', '302')

print(num.count('1'))

# 32