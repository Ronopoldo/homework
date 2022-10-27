# ###################3
# print(int('4030', 5))


###################### 7

# num = 4 ** 16 + 2 ** 34 - 8
# print(bin(num))
# print(bin(num).count('1'))



'''

Тип 1 № 18809
На рисунке справа схема дорог Н-ского района изображена в виде графа; в таблице слева содержатся сведения о протяжённости каждой из этих дорог (в километрах).



П1	П2	П3	П4	П5	П6	П7
П1		11	5		12
П2	11		8	15		23
П3	5	8			10		7
П4		15				10
П5	12		10				11
П6		23		10
П7			7		11


Так как таблицу и схему рисовали независимо друг от друга, то нумерация населённых пунктов в таблице никак не связана с буквенными обозначениями на графе. Определите, какова длина дороги из пункта В в пункт Г. В ответе запишите целое число — так, как оно указано в таблице.


Ответ:
8
2
Тип 1 № 38446
На рисунке схема дорог N-ского района изображена в виде графа, в таблице содержатся сведения о протяжённости каждой из этих дорог (в километрах).



П1	П2	П3	П4	П5	П6	П7
П1		3			4
П2	3				12	13
П3				10	11
П4			10		9		7
П5	4	12	11	9		8	6
П6		13			8		5
П7				7	6	5




Так как таблицу и схему рисовали независимо друг от друга, то нумерация населённых пунктов в таблице никак не связана с буквенными обозначениями на графе. Определите, какова сумма протяжённостей дорог из пункта Б в пункт В и из пункта Г в пункт Д.

В ответе запишите целое число.


Ответ:
20
3
Тип 8 № 39237
Все четырёхбуквенные слова, в составе которых могут быть только буквы А, В, Т, О, Р, записаны в алфавитном порядке и пронумерованы, начиная с 1. Ниже приведено начало списка:

1. АААА

2. АААВ

3. АААО

4. АААР

5. АААТ

6. ААВА

Под каким номером в списке идёт слово ТАРА?


Ответ:
516
4
Тип 11 № 10476
При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из 10 символов и содержащий только символы из 26-символьного набора латинского алфавита. В базе данных для хранения сведений о каждом пользователе отведено одинаковое и минимально возможное целое число байт. При этом используют посимвольное кодирование паролей, все символы кодируют одинаковым и минимально возможным количеством бит. Кроме собственно пароля, для каждого пользователя в системе хранятся дополнительные сведения, для чего выделено целое число байт; это число одно и то же для всех пользователей.

Для хранения сведений о 10 пользователях потребовалось 500 байт. Сколько байт выделено для хранения дополнительных сведений об одном пользователе? В ответе запишите только целое число — количество байт.


Ответ:
43
5
Тип 13 № 29122
На рисунке — схема дорог, связывающих пункты А, Б, В, Г, Д, Е, Ж, И, К, Л, М, Н, П. Сколько существует различных путей из пункта А в пункт П, проходящих через пункт Е и при этом не проходящих через пункт Л?




Ответ:
14
6
Тип 13 № 5216
На рисунке изображена схема дорог, связывающих города A, B, C, D, E, F, G, H, K, L, M. По каждой дороге можно двигаться только в одном направлении, указанном стрелкой. Сколько существует различных путей из города A в город M?



Ответ:
39
7
Тип 14 № 18085
Значение выражения 416 + 234 − 8 записали в системе счисления с основанием 2. Сколько цифр 1 содержится в этой записи?


Ответ:
30

'''



num = 0
for x1 in range(0, 5):
    for x2 in range(0, 5):
        for x3 in range(0, 5):
            for x4 in range(0, 5):
                num = num + 1
                s = str(x1) + str(x2) + str(x3) + str(x4)
                if (str(s).count('4030') == 1):
                    print(num)
                # print(s)