s = open('17.txt').read().split('\n')

print(s)
counter = 0
maxS = 0
for s1 in range(10000):
    for s2 in range(s1 + 1, 10000):
        if (int(s[s1]) + int(s[s2])) % 80 and ((int(s[s1]) % 50 == 0) or (int(s[s2]) % 50 == 0)):
            counter+=1
            maxS = max(maxS, int(s[s1]) + int(s[s2]))

        print(s1, s2)

print(counter, maxS)