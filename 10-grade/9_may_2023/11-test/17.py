f = open('17.txt').read()
f = f.split('\n')
print(f)

chet = 0
amount = 0
for i in range(len(f)):
    if int(f[i]) % 2 == 0:
        chet = chet + int(f[i])
        amount += 1

srZn = chet / amount
print(chet, amount, srZn)


out = []

for i in range(len(f) - 1):
    if (int(f[i]) % 3 == 0 or int(f[i+1]) % 3 == 0) and (int(f[i]) < srZn or int(f[i+1]) < srZn):
        out.append(int(f[i]) + int(f[i+1]))

print(out)
print(len(out))
print(max(out))