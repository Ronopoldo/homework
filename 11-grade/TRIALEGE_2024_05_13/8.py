from itertools import product
i = 0

for combo in product('ACBX', repeat=5):
    word = ''.join(combo)
    if word.count('X') == 1:
        i+=1
        print(word)

print(i)