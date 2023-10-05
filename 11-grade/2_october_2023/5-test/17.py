s = list(map(int, open('17.txt')))
answers = []

for x in range(len(s)-1):
    for y in range(x+1, len(s)):
        if ((s[x] + s[y]) % 80 == 0) and ((s[x] % 50 == 0) or (s[y] % 50 == 0)):
            print('gotcha')
            answers.append(s[x] + s[y])
    # print(x)



print(answers)

print(len(answers), max(answers))
    #21648 19760