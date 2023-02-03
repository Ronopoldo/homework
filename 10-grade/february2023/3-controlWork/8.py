N = 25 ** 6 + 5 ** 18 - 5
# N = 80
out = ''
while N > 0:
    out = str(N % 5) + out
    N = N // 5

print(out)
print(out.count('4'))
#3814941406245
#3814941406245

print(3814941406245 == 3814941406245)

# 11