# 	(№ 2250) Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на
# 	натуральное число m». Для какого наибольшего натурального числа A формула
# (ДЕЛ(x, 40) ∨ ДЕЛ(x, 64)) → ДЕЛ(x, A)
#
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?

# ПЕРЕБОР
# i = 0
# for a in range(500, 0, -1):
#     for x in range(1, 1000):
#         if (((x % 40 == 0) or (x % 64 == 0)) <= (x % a == 0)) == 1:
#             i += 1
#             if (i == 999):
#                 print(a)
#     i = 0
#


# ЛОГИКА
for a in range(5000, 0, -1):
    flag =  False
    for x in range(1, 20000):
        if (((x % 40 == 0) or (x % 64 == 0)) <= (x % a == 0)) == 0:
            flag = True
            break
    if flag == False:
        print(a)
