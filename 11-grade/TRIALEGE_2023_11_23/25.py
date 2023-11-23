# from fnmatch import fnmatch
#
# for i in range(Начало, конец, делитель на который нацело делица):
#     if fnmatch(str(i), 'МАСКА'):
#         print(То что нужно вывести, например i – само число)

def dels(n):
    outArray = []
    for i in range(1, n+1):
        if n % i == 0:
            outArray.append(i)
    return outArray




def m(n):
    temp = dels(n)
    if len(temp) < 6:
        return 0
    else:
        return temp[1] * temp[2] * temp[3] * temp[4] * temp[5]


for i in range(200000000, 10000000*100):
    if 0<m(i)<i:
        print(m(i))



'''

1728
21632
1260
1152
4127787
'''