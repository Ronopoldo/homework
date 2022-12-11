for i in range(100,1000):
    n1 = int(str(i)[0]) + int(str(i)[1])
    n2 = int(str(i)[1]) + int(str(i)[2])
    if ((sorted([str(n1),str(n2)])[::-1][0] + sorted([str(n1),str(n2)])[::-1][1]) == '1711'):
        print(i, sorted([str(n1),str(n2)])[0] + sorted([str(n1),str(n2)])[1])