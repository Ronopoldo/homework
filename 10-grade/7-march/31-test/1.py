num = '2' * 247

while ('222' in num) or ('555' in num):
    if '222' in num:
        num = num.replace('222', '5', 1)
    else:
        num = num.replace('555', '2', 1)

print(num)

# 552
