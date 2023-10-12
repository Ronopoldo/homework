from math import *

mMax = int(log(400_000_000, 2))+1
nMax = int(log(400_000_000, 3))+1

answers = []

for m in range(0, mMax, 2):
    for n in range(1, nMax, 2):
        if (200_000_000 <= (2 ** m * 3 ** n) <= 400_000_000):
            answers.append(2 ** m * 3 ** n)

print(sorted(answers))