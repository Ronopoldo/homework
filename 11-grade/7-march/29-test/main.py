s = open('1_2.txt', encoding='utf8').read()

s = s.replace('\n', ' ')
# s = s.replace("\", ' ')
s = s.replace('-', ' ')
s = s.replace('?', ' ')
s = s.replace('!', ' ')
s = s.replace(',', ' ')
s = s.replace('.', ' ')
s = s.replace('–', ' ')
s = s.replace('…', ' ')
# s = s.replace('»', ' ')
# s = s.replace('«', ' ')
# s = s.replace(':', ' ')
# s = s.replace('(', ' ')
# s = s.replace(')', ' ')

f = s.split(' ')
i = 0

for ele in f:
    if len(ele) == 3:
        i+=1


print(f)
print(i)

print(f.count('\xa0'))