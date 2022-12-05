for i in range(1000,10000):
    s = str(i)
    x1 = int(s[0]) * int(s[1])
    x2 = int(s[2]) * int(s[3])
    array = sorted([x1,x2])[::-1]
    if (str(array[0]) + str(array[1]) == '124'):
        print(i, x1,x2)
        break