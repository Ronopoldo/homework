# Способ 1

f = open('27691.txt').readline()
#print(f)
max1 = 0
temp = 0

for i in range(len(f)):
    if f[i] == 'A':
        temp += 1
    else:
        temp = 0
    if (temp > max1):
        max1 = temp
    #print(i, len(f))

print(max1)


# Способ 2
s = open('27691.txt').readline()

s = s.replace('B', ' ').replace('C', ' ')
s = s.split()

print(max(s, key = len), len(max(s, key = len)))