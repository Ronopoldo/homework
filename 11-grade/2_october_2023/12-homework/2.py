def div(n):
    out = []
    for i in range(1, n + 1):
        if (n % i == 0) and (i % 2 != 0):
            out.append(i)
    return out


counter = 1
for num in range(95632, 95651):
    if len(div(num)) == 6:
        print(div(num))