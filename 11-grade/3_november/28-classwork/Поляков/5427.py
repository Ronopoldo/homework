from itertools import product

i = 0
nums = '023'
doubles = ['ГГ', 'ЕЕ', 'КК', 'ЭЭ', '00', '22', '33']
for word in product('ГЕКЭ023', repeat = 4):
    i+=1

    if word[0] in nums and 'ГГ' not in word and 'ЕЕ' not in word and 'КК' not in word and  'ЭЭ' not in word and  '00' not in word and  '22' not in word and  '33':
        print(word, i)