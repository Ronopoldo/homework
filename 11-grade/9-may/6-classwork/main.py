s = list(map(int, open('2_17.txt').read().split('\n')))

maxi = -1

for ele in s:
    if (str(abs(ele))[-2::] == '21') and (len(str(abs(ele))) == 5):
        maxi = max(maxi, ele)

output = []

for x in range(len(s) - 1):
    y = x + 1
    isFirst = (str(abs(s[x]))[-2::] == '21') and (len(str(abs(s[x]))) == 5)
    isSecond = (str(abs(s[y]))[-2::] == '21') and (len(str(abs(s[y]))) == 5)
    if isFirst ^ isSecond :
        if (s[x] ** 2 + s[y] ** 2) >= (maxi ** 2):
            output.append(s[x] + s[y])
    # print(f'Готово: {x / len(s) * 100}%')

print(len(output), max(output))
