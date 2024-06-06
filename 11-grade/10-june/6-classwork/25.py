def findDels(num):
    out = []
    for i in range(1, num + 1):
        if num % i == 0:
            if i % 2 == 0:
                out.append(i)
    return out

from fnmatch import fnmatch

def summa(arr):
    out = 0
    for ele in arr:
        out+=ele
    return out


i = 0

for num in range(65001, 932932929):
    if i <= 7:
        if fnmatch(str(num), '6*97*5?') == True:
            if len(findDels(num)) >= 4:
                print(num, summa(findDels(num)))
                i+=1