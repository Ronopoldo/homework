# f = open('24.txt').readline()
# tmp = 0
#
# for i in range(len(f)-1):
#     if (f[i] == 'K' and f[i+1] != 'L') or (f[i] == 'L' and f[i+1] != 'K') or (f[i] != 'K' and f[i] != 'L') or (f[i+1] != 'K' and f[i+1] != 'L'):
#         tmp+=1
# print(tmp)


f = str(open('24.txt').readline())

print(len(f))
f = f.replace('KL', '*')
f = f.replace('LK', '*')
f = f.split('*')

print(len(max(f, key=len)))