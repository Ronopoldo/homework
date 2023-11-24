from itertools import product
arrange = product('0123456789ABCDE', repeat = 5)
counter = 0
for originNumber in arrange:
    num = ''.join(originNumber)
    if num[0] != '0':
        num = num.replace('C', '@').replace('6', '@')
        num = num.replace('2', '$').replace('4', '$').replace('A', '$').replace('8', '$').replace('E', '$')
        num = num.replace('3', '%').replace('9', '%')
        num = num.replace('1', '!').replace('D', '!').replace('0', '!').replace('5', '!').replace('7', '!').replace('B', '!')
        num = num.replace('!', '')
        if ('$$' not in num) and ('%%' not in num) and ('@' not in num):
            counter+=1
            print(num)
print(counter)