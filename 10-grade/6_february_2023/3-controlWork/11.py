def f(m,n):
    return m & n

# print(f(14,5))

#
# for A in range(0, 8192):
#     i = 0
#     for x in range(0, 1024):
#         if ((f(x, 77) != 0) <= ((f(x,12) == 0) <= (f(x,A) != 0))) == 1:
#             i = i + 1
#         if i == 1024:
#             print(A)
#             break




for A in range(0, 8192):
    i = 0
    for x in range(0, 1024):
        if (x&77 !=0) <= ((x&12==0) <= (x&A!=0)):
            i+=1
        if i == 1024:
            print(A)
            print('2nd')
            break



print('2nd')

# i = 0
# for x in range(0, 1024):
#     i = i + 1
# print(i)


# 65 (ПРОВЕРИТЬ)
# ПРОВЕРЕНО