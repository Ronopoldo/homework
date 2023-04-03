num = '8' * 70

while '2222' in num or '8888' in num:
    if '2222' in num:
        num = num.replace('2222', '88', 1)
    else:
        num = num.replace('8888', '22', 1)

print(num)

# 4 (22)
