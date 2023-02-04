from itertools import product

arrange = product('НРТУ', repeat = 4)
i = 0

for word in arrange:
    i+=1
    if i == 215:
        print(word)
#УРРТ