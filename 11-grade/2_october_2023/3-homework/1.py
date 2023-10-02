s = open('24.txt').readline().split('A')

maxSize = 0

for i in range(len(s) - 1):
    maxSize = max(maxSize, int(len(s[i])) + int(len(s[i+1])) + 1)

print(maxSize)