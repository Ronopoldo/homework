s = open('24.txt').read()

maxi = -1
temp = 0
for i in range(1, len(s)):
    if s[i] <= s[i-1]:
        temp+=1
    else:
        maxi = max(maxi, temp)
        temp = 1

print(maxi)