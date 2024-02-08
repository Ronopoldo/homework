def findDels(num):
    out = []
    for i in range(1, round(num ** 0.5)):
        if num % i == 0:
            out.append(i)
            out.append(num // i)
    out = sorted(out)
    return out



for x in range(174457, 174506):
    if len(findDels(x)) == 4:
        print(findDels(x)[1], findDels(x)[2])