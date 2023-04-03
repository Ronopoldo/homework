from itertools import permutations

arrange = permutations('1' * 50 + '2'* 50 + '3'*50)

for num in arrange:
    s = ''.join(num)
    while '13' in s or '32' in s or '12' in s:
        s = s.replace('13','31',1)
        s = s.replace('32','23',1)
        s = s.replace('12', '21', 1)

    print(s[9],s[69],s[139])