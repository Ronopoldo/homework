from itertools import permutations

maxi = 0

s = open('24.txt').read()
t = s.replace('XYZ', '*')
t = t.replace('XZY', '*')
t = t.replace('YZX', '*')
t = t.replace('YXZ', '*')
t = t.replace('ZXY', '*')
t = t.replace('ZYX', '*')
t = t.split('*')

print(t)
for ele in t:
    maxi = max(maxi, len(ele))


for ele in t:
    if len(ele) == maxi:
        print(s[s.index(ele)-5], s[s.index(ele)-4], s[s.index(ele)-3], s[s.index(ele)-2], s[s.index(ele)-1], '-==', s[s.index(ele)],  s[s.index(ele) + 1], '===', s[s.index(ele)+maxi-1], s[s.index(ele)+maxi] + '===-', s[s.index(ele)+1+maxi], s[s.index(ele)+2+maxi], s[s.index(ele)+3+maxi], s[s.index(ele)+4+maxi], s[s.index(ele)+5+maxi])

print(maxi)



# 15729






