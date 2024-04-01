def f(s, m):
    if s >= 70: return (m % 2) == 0
    if m == 0: return 0
    h = [
        f(s + 1, m - 1),
        f(s + 4, m - 1),
        f(s * 5, m - 1)
    ]
    if ((m - 1) % 2) != 0:
        return all(h)
    else: return any(h)

print('ЗАДАНИЕ 19 ')
for s in range(1, 70):
    if f(s, 2):
        print(s)
        break

print('ЗАДАНИЕ 20 ')
for s in range(1, 70):
    if f(s, 3) and (not f(s, 1)):
        print(s)



print('ЗАДАНИЕ 21 ')

for s in range(1, 70):
    if f(s, 4) and (not f(s, 2)):
        print(s)




# 912
#
# 8





# def f(s, m):
#   if s >= 70: return (m % 2) == 0
#   if m == 0: return 0
#
#   h = [
#     f(s + 1, m - 1),
#     f(s + 4, m - 1),
#     f(s * 5, m - 1)
#   ]
#
#   if (m - 1) % 2 == 0:
#     return any(h)
#   else:
#     return all(h)
#
# for s in range(70):
#   if f(s, 3) and not f(s,1):
#     print(s)
