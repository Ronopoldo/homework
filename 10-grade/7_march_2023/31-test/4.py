num = '>' + '1' * 25 + '2' * 17 + 10 * '3'

while '>1' in num or '>2' in num or '>3' in num:
    if '>1' in num:
        num = num.replace('>1', '22>3', 1)
    if '>2' in num:
        num = num.replace('>2', '2>', 1)
    if '>3' in num:
        num = num.replace('>3', '11>2', 1)

print(num.count('2') * 2 + num.count('1'))

# 13 (274)