s = open('24.txt').read().split('\n')

def searchDelta(arr):
    outArr = []
    for x in range(len(arr) - 1):
        for y in range(len(arr)):
            if arr[x] == arr[y]:
                outArr.append(abs(y-x))
                break

    return outArr[:-1:]

maxList = []

for line in s:
    if line.count('A') < 25:
        maxList.append(max(searchDelta(list(line))))


print(max(maxList))


# 1004