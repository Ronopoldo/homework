for A in range(-128,1024):
    i = 0
    for x in range(0, 256):
        for y in range(0, 256):
            if ((x < A) <= (x**2 < 81) and ((y**2 <= 36) <= (y<=A))) == 1:
                i+=1
    if i == 65536: # 256 * 256
        print(A)


        # 4 ШТ

# i = 0
# for x in range(0, 256):
#     for y in range(0, 256):
#         i+=1
# print(i)
