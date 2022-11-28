# # 61446
# from itertools import product
# arrange = product('АНТИУОПЯ', repeat = 16)
#
# sogl = ['Н', 'T', 'П']
# glas = ['А', 'И', 'У', 'О', 'Я']
#
# debugCount = 0
# for i in arrange:
#   if debugCount > 16777216:
#     word = ''.join(i)
#     if 'АНТИУТОПИЯ' in word:
#       print(word)
#       word = word.replace('АНТИУТОПИЯ', '')
#       print(word)
#       print()
#   debugCount+=1
#   print(str(debugCount) + '/281474976710656') # str(round(debugCount/281474976710656*100,2)) + '%'





# 61446
from itertools import product
count = 0
debugCount = 0
iterations = 0
for i in range(7):
  arrange = product('АНТИУОПЯ', repeat=i)
  for i1 in arrange:
    preword = ''.join(i1) + 'АНТИУТОПИЯ'
    arrange2 = product('АНТИУОПЯ', repeat=16-len(preword))
    for i2 in arrange2:
      iterations += 1
      word = preword + ''.join(i2)
      print(word)
      word = word.replace('АНТИУТОПИЯ', '')
      print(word)
      glasses = word.replace('Н', '').replace('Т', '').replace('П', '')
      soglasses = word.replace('А', '').replace('И', '').replace('О', '').replace('У', '').replace('Я', '')
      print(glasses, ''.join(sorted(glasses)[::-1]), glasses == ''.join(sorted(glasses)[::-1]))
      print(soglasses, ''.join(sorted(soglasses)), soglasses == ''.join(sorted(soglasses)))
      print('=' * round(iterations / 1835008 * 100) + '-' * (100 - round(iterations / 1835008 * 100)) + str(round(iterations / 1835008 * 100 , 5)) + '%')
      print()
      if soglasses == ''.join(sorted(soglasses)) and glasses == ''.join(sorted(glasses)[::-1]) and len(soglasses) <= 2:
        count += 1



  print(str(count) + ' раз встречается искомое число\n' + str(iterations) + ' операций было выполнено (упрощённый алгоритм)')


# word = 'АБРОКЫДАБРА'
# glas = 'АОЫ'
#
# print(sorted(word)[::-1])