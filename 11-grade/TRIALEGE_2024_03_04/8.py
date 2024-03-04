from itertools import product

out = 0

for combo in product(['1','0'],repeat=11):
  c = ''.join(combo)
  if c.count('1') == 3 and ('11' not in c):
    # print(c)
    tmp = 1
    for i in range(len(c)):
      if i == 0 and c[i] == '0':
        tmp = tmp * 3
      else:
        tmp = tmp * 4
  
    out = out + tmp

print(out)

# 293 601 280


# 9992901218