s = open('24.txt').read()

s = s.replace('Q', '*')
s = s.replace('R', '*')
s = s.replace('S', '*')
print(s)
out = []

n = s.split('**')

print(len(max(n, key = len)) + 2)