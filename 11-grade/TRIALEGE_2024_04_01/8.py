from itertools import product
i = 0
for combo in product('МСТФ', repeat=4):
    i+=1
    print(i, combo)
    if i == 138:
        print(combo)


# n = 138
# ost = ''
# while n > 0:
#     ost = str(n % 4) + ost
#     n//=4
#
# print(ost)