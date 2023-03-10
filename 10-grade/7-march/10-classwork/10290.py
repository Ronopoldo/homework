s = '1' + '8' * 80
while ('18' in s) or ('288' in s) or ('3888' in s):
    s = s.replace('18', '2',1)
    s= s.replace('288', '3',1)
    s=s.replace('3888', '1',1)
print(s)