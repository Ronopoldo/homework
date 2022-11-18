#4 задача

array = [1,-8,0,-985,789,-5,-8,-101,45]
array2 = []
array3 = []
array4 = []
output = []
for i in range(len(array)):
    array2.append(abs(array[i]))


for i2 in range(len(array)):
    print(array[i2])
    if array[i2] < 0:
        array3.append(True)
    else:
        array3.append(False)

print(array)
print(array2)
print(array3)

array4 = array4 + array2
array4.sort()
print(array4)
print()
for i3 in range(len(array)):
    if array3[array2.index(array4[i3])] == True:
        output.append(0-array4[i3])
        print(True)
    else:
        output.append(array4[i3])
output.reverse()
print(output)