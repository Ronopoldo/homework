s = open('29672.txt').read().split('\n')
counter = 0
for i in s:
    if i.count('E') > i.count('A'):
        counter+=1
print(counter)