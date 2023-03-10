s = '4' * 9 + '5' * 12
while '444' in s or '888' in s:
    s = s.replace('444', '8', 1)
    s = s.replace('555', '8')
    s = s.replace('888', '3')

print(s)