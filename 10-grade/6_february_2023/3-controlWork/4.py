for N in range(2, 8192):
    R = str(bin(N)[2::])
    i = 0
    newR = ''
    while i < (len(R) - 1):
        newR = newR + R[i]
        i = i + 1
    newR = newR + str(R[1]) + str(R[1])
    print(int(newR, 2))
    if (int(newR, 2) > 76):
        print(newR, N, R, bin(N))
        print(int(newR, 2))
        print(N)
        break
# 40


# 10011
# 101000
# 1010000


# R = '101001'
# i = 0
# newR = ''
# while i < len(R) - 1:
#     newR = newR + R[i]
#     i = i + 1
#
# print(newR)

