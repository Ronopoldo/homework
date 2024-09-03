def min_count(n):
    k = 0
    array = []

    for ele in s.split(' '):
        array.append(int(ele))

    while (len(array) > 0) and (array != [0] * len(array)):
        if 0 not in array:
            array = [x - 1 for x in array]
            k += 1
        elif array[0] == 0:
            while array[0] == 0:
                array.pop(0)
                if len(array) == 0:
                    break
        else:
            array = [x - 1 for x in array[0:array.index(0)]] + array[array.index(0):len(array)]
            k += 1
    return k


s = str(input())
print(min_count(s))
