s = open('56554.txt').read().split('\n')

matrixW = -1

for ele in s:
    matrixW = max(matrixW, int(ele.split(' ')[0]))

matrix = [['0'] * matrixW] * len(s)

for ele in s:
    matrix[int(ele.split(' ')[0])][int(ele.split(' ')[1])] = '1'

newMatrix = []
print(len(matrix))

for raw in matrix:
    newMatrix.append(''.join(raw))

print(newMatrix[23])


# for ele in s:
