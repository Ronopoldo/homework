from itertools import permutations

i = 0

arr = set()

for combo in permutations('КАПКАН'):
    word = ''.join(combo)
    if ('КК' not in word) and ('АА' not in word):
        arr.add(word)

print(len(arr))