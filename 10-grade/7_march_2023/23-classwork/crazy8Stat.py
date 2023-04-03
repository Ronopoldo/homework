from itertools import product

arrange = product('012345678', repeat = 11)

non = ['1','3','5','7']
i = 0

for word in arrange:
    temp = 0
    i1 = 0
    for i1 in range(10):
        if word[i1] in non:
            temp+=1
        if word[i1] in non and word[i1 + 1] in non and i1 != 10:
            break
            i1 = 17890
    if temp == 3:
        i+=1

    print(i)


print(i)