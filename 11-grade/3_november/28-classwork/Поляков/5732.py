from itertools import product

print(sorted('ТИМАШЕВСК'))
i = 0
sogl = 'ШТСМКВ'

for word in product('ШТСМКИЕВА', repeat = 5):
    i+=1
    if word[2] in sogl:
        if (word[0] not in sogl) and (word[1] not in sogl) and (word[3] not in sogl) and (word[4] not in sogl):
            if word[0] + word[1] == word[3] + word[4]:
                print(i)