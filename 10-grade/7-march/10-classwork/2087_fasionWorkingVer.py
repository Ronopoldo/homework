origin = '1111111111'

for i in range(32):
  for i1 in range(i + 1):
    answer = origin.replace('1','5',i1)
    answer = answer + '2' * (i-i1)
    answer = int(answer)
    #print(answer)
    output = answer
    sum = 0
    while (answer != 0):
      sum = sum + answer % 10
      answer = answer // 10  

    if (sum == 34):
      print(f'Gotha! {output,i}')