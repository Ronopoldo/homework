s = open('6606.txt').read()

s = s.replace('EA', '**')
s = s.replace('NPC', '***')

maxi = -1

i = 0
while '*' * i in s:
    maxi = i
    i += 1

print(maxi)
