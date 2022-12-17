for i in range(10000, 100000):
    num1 = int(str(i)[0]) + int(str(i)[2]) + int(str(i)[4])
    num2 = int(str(i)[1]) + int(str(i)[3])
    output = str(sorted([num1, num2])[0]) + str(sorted([num1, num2])[1])
    if output == '621':
        print(i, output)
        break