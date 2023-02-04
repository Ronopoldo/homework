for x in range(0,11):
    n1 = ('8' + str(x) + '71')
    n2 = ('3' + str(x) + 'DF')
    if (int(n1 , 13) + int(n2 , 17)) % 197 == 0:
        print(x,  (int(n1 , 13) + int(n2 , 17)) / 197)

# 175