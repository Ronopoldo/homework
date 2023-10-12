def div(x):
    d = set()
    if int(x ** 0.5) == x ** 0.5:
        for i in range(2, int(x ** 0.5) - 1):
            if len(d) <= 2:
                if x % i == 0:
                    d.add(i)
                    d.add(x // i)
            else: return [False]
        return [len(d) == 2, d]
    return [False]


for num in range(123456789, 223456789 + 1):
    if div(num)[0]:
        print(num, max(div(num)[1]))
    # print(num, div(num))