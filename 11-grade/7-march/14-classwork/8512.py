s = open('8512.txt').read().split('\n')
sNew = []

for ele in range(len(s)):
    sNew+=['']
    sNew[ele] = [int((s[ele].split(' '))[0]), int((s[ele].split(' '))[1])]

sNew = sorted(sNew)
boxes = [0 for i in range(210)]

print(sNew)
passengers = 0
lastBox = -1

for time in range(1440):
    for box in range(len(boxes)):
        if time == boxes[box]:
            boxes[box] = 0

    for ele in sNew:
        if ele[0] == time:
            if 0 in boxes:
                lastBox = boxes.index(0) + 1
                boxes[boxes.index(0)] = ele[1] + 1
                passengers+=1


print(passengers, lastBox)
