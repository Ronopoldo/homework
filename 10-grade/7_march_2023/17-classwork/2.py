from itertools import permutations

arrange = permutations('1' * 11 + '2'* 12 + '3'*30)

for num in arrange:
    s = '>' + ''.join(num)
    #print(s)

    while '>1' in s or '>2' in s or '>3' in s:
        s = s.replace('>1', '22>',1)
        s = s.replace('>2', '2>',1)
        s = s.replace('>3', '1>', 1)
    s = s.replace('>', '')
    #print(int(s))

    k = 0
    for elem in s:
        if elem.isdigit():
            k += int(elem)
    print(k)