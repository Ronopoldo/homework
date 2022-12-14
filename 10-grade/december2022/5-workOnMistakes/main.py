from itertools import product

arrange = product('АНДРЕЙ', repeat = 7)
i = 0

for word in arrange:
    if (word.count('А') == 1 and word.count('Й') == 1 and word[0] != 'Й'):
        i+=1

print(i)


#
# from itertools import product
#
# arrange = product('12345', repeat = 5)
# i = 0
#
# for word in arrange:
#     if (word.count('1') == 3):
#         i+=1
#         print(word,word.count('1'))
#
# print(i)


# from itertools import product
#
# arrange = product('АНДРЕЙ', repeat = 7)
# i = 0
#
# for word in arrange:
#     if (word.count('А') == 1 and word.count('Й') == 1 and word[0] != 'Й'):
#         i+=1
#
#
# print(i)
#



# from itertools import product
#
# arrange = product('12345', repeat = 5)
# i = 0
# for word in arrange:
#     if (word.count('1') == 3):
#         i+=1
#
# print(i)



'''
Тип 8
Алексей составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово. В качестве кодовых слов Алексей использует 5-буквенные слова, в которых есть только буквы A, B, C, X, причём буква X может появиться на первом месте или не появиться вовсе. Сколько различных кодовых слов может использовать Алексей?


Ответ:
324
2
Тип 8
Все четырёхбуквенные слова, в составе которых могут быть только буквы А, В, Т, О, Р, записаны в алфавитном порядке и пронумерованы, начиная с 1. Ниже приведено начало списка:

1.  АААА

2.  АААВ

3.  АААО

4.  АААР

5.  АААТ

6.  ААВА

Под каким номером в списке идёт слово ВАТА?


Ответ:
146
3
Тип 8
Все 5-буквенные слова, составленные из букв А, О, У, записаны в алфавитном порядке. Вот начало списка:



1.  ААААА

2.  ААААО

3.  ААААУ

4.  АААОА

……



Укажите номер слова ОАОАО.


Ответ:
92
4
Тип 8
Андрей составляет 7-буквенные коды из букв А, Н, Д, Р, Е, Й. Буквы А и Й должны встречаться в коде ровно по одному разу, при этом буква Й не может стоять на первом месте. Остальные допустимые буквы могут встречаться произвольное количество раз или не встречаться совсем. Сколько различных кодов может составить Андрей?


Ответ:
36684
5
Тип 8
Все 5-буквенные слова, составленные из букв А, О, У, записаны в алфавитном порядке. Вот начало списка:



1.  ААААА

2.  ААААО

3.  ААААУ

4.  АААОА

……



Укажите номер слова УАУАУ.


Ответ:
183
6
Тип 8
Шифр кодового замка представляет собой последовательность из пяти символов, каждый из которых является цифрой от 1 до 5. Сколько различных вариантов шифра можно задать, если известно, что цифра 1 встречается ровно три раза, а каждая из других допустимых цифр может встречаться в шифре любое количество раз или не встречаться совсем?


Ответ:
160
7
Тип 8
Сколько слов длины 4, начинающихся с согласной буквы, можно составить из букв Л, Е, Т, О? Каждая буква может входить в слово несколько раз. Слова не обязательно должны быть осмысленными словами русского языка.


Ответ:
128

'''