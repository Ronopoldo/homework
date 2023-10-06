from fnmatch import *

def div(n):
    summarDivs = 0
    chetDivs = 0
    for i in range(1, n+1):
        if n % i == 0:
            if i % 2 == 0:
                chetDivs+=1
                summarDivs = summarDivs + i
    return [summarDivs, chetDivs]


print(div(3267))
i = 0
for n in range(65000, 90000000000):
    if (fnmatch(str(n), '6*97*5?')) and (div(n)[1] >= 4):
        print(n, str(div(n)[0
                     ]))
    # if (div(n)[1] >= 4):
    #     i+=1
    # print(i)
    # print(n, div(n), (fnmatch(str(n), '6*97*5')))


'''
69750 129792
69752 122080
69756 139536
69758 75152
609750 1103232
609752 1291248
609754 630840

'''