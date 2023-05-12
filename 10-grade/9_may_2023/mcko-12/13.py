f = open('13.txt').read().split('\n')
#f = [6,42,14,-28,6]

final = []
for i in range(0, len(f)-1):
    if int(f[i]) % 14 == 0 and int(f[i+1]) % 14 == 0:
        final.append(int(f[i]) + int(f[i+1]))


print(final)
print(len(final), max(final))