def find5Dels(num):
    out = []
    for i in range(2, round(num ** 0.5)):
        if num % i == 0:
            out.append(i)
            out.append(num // i)

    out = sorted(out)
    if len(out) < 5: return [0]
    return out


def multiply(arr):
    out = 1
    tempVar = 0
    for ele in arr:
        out*=ele
        tempVar+=1
        if tempVar > 4:
            break
    return out

tema = 0
for N in range(200_000_001, 256256256256):
    if (0<(multiply(find5Dels(N)))< N) and (tema < 5):
        print(multiply(find5Dels(N)), N)
        tema+=1
    # print(N)


        #
        # список.index(элемент)

        # [1,2,3,4].index(3) => 2