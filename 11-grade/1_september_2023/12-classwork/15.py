# for A in range(1024):
#     i = 0
#     for x in range(256):
#         for y in range(256):
#                 if (x + 2 * y < A) or (y > x) or (x > 60):
#                     i+=1
#
#     if i == 65536:
#         print(A)


# def f(x,y,A):
#     return (x + 2 * y < A) or (y > x) or (x > 60)
#
# for a in range(0, 1000):
#     if all(f(x,y,a) == 1 for x in range (0,1000) for y in range(0, 1000)):
#         print(a)