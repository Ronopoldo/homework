n = '1' * 45 + '2' * 45
while '111' in n:
    n = n.replace('111','2',1)
    n= n.replace('222','1',1)

print(n)
# 12

# 224