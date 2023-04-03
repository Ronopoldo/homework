def counter(num):
    out = 0
    s = list(str(num))
    for i in range(len(s)):
        out += int(s[i])
    return out


# print(counter(187))
#

for n in range(32):
    num = '9' + '1' * n + '2' * n
    while ('91' in num) or ('92' in num):

        if '91' in num:
            num = num.replace('91', '39', 1)
        if '92' in num:
            num = num.replace('92', '59', 1)

    print(n, counter(num))

# 13 (для 113)
