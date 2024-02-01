s = open('24-1.txt').read()

outerFinal = []

for i1 in range(len(s) // 10):
    for i2 in range(i1 + 1, len(s)):
        if list(s[i1:i2]) == sorted(s[i1:i2]) and ((i2 == i1) or (s[i2] != s[i2-1])):
            print("TRUE")
            outerFinal.append(s[i1:i2])
        else:
            print( list(s[i1:i2]) , sorted(s[i1:i2]), i1, i2)
            break

    print(i1/len(s) * 100, i1, len(s))

print(outerFinal)
print(max(outerFinal, key=len))