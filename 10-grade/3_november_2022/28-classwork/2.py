from itertools import product
arrange = product('АПРСУ', repeat = 5)
counter = 0
for word in arrange:
    counter += 1
    slovo = ''.join(word)
    if slovo == 'УАПАП':
        print(counter, slovo)