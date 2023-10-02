delits = 0

def findDels(num):
    output = []
    for i in range(1, num + 1):
        if num % i == 0:
            output.append(i)
    return output

for n in range(84052, 84131):
    if len(findDels(n)) > delits:
        delits = len(findDels(n))
        correctNumber = n

print(delits,correctNumber)