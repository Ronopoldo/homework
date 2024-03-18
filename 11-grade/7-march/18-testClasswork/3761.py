s = list(map(int, open('3761.txt').read().split('\n')))

pairsAmount = 0
maxAverage = 0
noReps = set(s)

for x in range(len(s)):
    for y in range(x + 1, len(s)):
        if (s[x] + s[y]) / 2 in noReps:
            pairsAmount += 1
            maxAverage = max(maxAverage, (s[x] + s[y]) / 2)

print(pairsAmount, int(maxAverage))
