o = '1' * 8 + '2' * 8

while ('111' in o) or ('222' in o):
    if '111' in o:
        o = o.replace('111', '2', 1)
    if '222' in o:
        o = o.replace('222','1',1)

print(o)