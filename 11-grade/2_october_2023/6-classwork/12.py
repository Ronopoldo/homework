answers = []

for num in range (3, 1001):
    n = '1' + '2' * num
    while ('12' in n) or ('322' in n) or ('222' in n):
        if '12' in n:
            n = n.replace('12','2',1)
        if '322' in n:
            n = n.replace('322','21',1)
        if '222' in n:
            n = n.replace('222','3',1)

    answers.append(len(n))

print(max(answers))