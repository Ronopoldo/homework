# x = 100000000
# danyasamiylutshiy = 'valavin'
# yaegolublucilno = 'lox'
# a = []
# while x>0:
#     a = [x%2]+a
#     x//=2
#     print(danyasamiylutshiy+yaegolublucilno)


s = open('24.txt').read().replace('RSQ', '*')
a = []

for i in range(1000):
    if '*' * i in s:
        a.append(i)

iPr = 0
indexList = []


##########
for i in range(s.count('*' * max(a))):
    iCur = s.index('*' * max(a), iPr)
    iPr = iCur + 1
    indexList.append(iCur)

for i in indexList:
    print(s[i-2:i+19])

##############




# for i in range(s.count('*' * max(a))):
#     iCur = s.index('*' * max(a), iCur + 1)
#     print(s[iCur-2:iCur+19])


maxi = max(a) * 3

for l in indexList:
    temp = max(a) * 3

    if s[l-1] == 'Q':
        temp+=1
        if s[l-2] == 'S':
            temp+=1

    if s[l+max(a)+1] == 'R':
        temp+=1
        if s[l+max(a)+2] == 'S':
            temp+=1

    maxi = max(maxi, temp)

print(maxi)