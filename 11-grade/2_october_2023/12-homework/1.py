def div(n):
    out = []
    for i in range(1, n + 1):
        if n % i == 0:
            out.append(i)
    return out


counter = 1
for num in range(245_690, 245_756):
    if len(div(num)) == 2:
        print(counter, num)
    counter+=1