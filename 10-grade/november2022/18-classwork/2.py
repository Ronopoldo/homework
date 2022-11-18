# 2 задача
array = list('программирование')
buffer = array[len(array)-1]
array[len(array)-1] = array[0]
array[0] = buffer
print(array)
