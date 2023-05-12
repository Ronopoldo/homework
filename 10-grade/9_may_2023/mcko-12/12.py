# i = 0
# for s in range(0,8192, 6):
#     s1 = s
#     n = 300
#     while s > 0:
#         s = s // 7
#         n = n // 3
#     if n == 11:
#         i+=1
#         print(s1)
#
# print(i)

i = 0
for s in range(65536):
    s1 = s
    n = 300
    while s > 0:
      s = s // 7
      n = n // 3
    if (n == 11) and (s % 6 == 0):
        i+=1
        print(s1)

print(i)