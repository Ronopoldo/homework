# def f(s,c,m):
#     if s >= 35: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s+1,c+1,m),f(s+2,c+1,m),f(s*2,c+1,m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h) # any(f) в конце для номера 15
#
# for s in range(1, 43):
#     for m in range(1,5):
#         if f(s,0,m) == 1:
#             print(s,m)
#
# '''
# 15) 9 (ПРОВЕРЕНО х2 ВРУЧНУЮ И ЧЕРЕЗ СИСТЕМУ)
# 16) 1516 (ПРОВЕРЕНО)
# 17) 14 (ПРОВЕРЕНО)
# '''



def f(s,c,m):
    if s >= 35: return c % 2 == m % 2
    if c == m: return 0
    h = [f(s+1,c+1,m),f(s+2,c+1,m),f(s*2,c+1,m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)

for s in range(1, 35):
    for m in range(1,5):
        if f(s,0,m) == 1:
            print(s,m)


