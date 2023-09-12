def counter(n):
    out = 0
    for i in range(len(n)):
        out += int(n[i])
    return out


def f(n):
    while ('52' in n) or ('2222' in n) or ('1122' in n):
        n = n.replace('52', '11', 1)
        n = n.replace('2222', '5', 1)
        n = n.replace('1122', '25', 1)
    # print(n)
    return n


# 156
max1 = 0
for num in range(4, 10000):
    # print(max1)
    if counter(str(f(num * '2'))) == 64:
        print(num)
        break
