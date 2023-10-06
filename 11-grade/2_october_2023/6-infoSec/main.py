# https://drive.google.com/file/d/18o9-gzr778Aso5ftQNuT52HaisT6pg_E/view

import random
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True




def generate_random_prime():
  print('ase')
  while True:
    print('1')
    num = random.randint(2**25, 2**38) ** 11 + 1
    print('2')
    print(f'trу{num}')
    if is_prime(num):
      return num
      prime('ae')

print(generate_random_prime())
print('ОТВЕТ ^^')

# int(str(random.randint(2**32, 2**33)) + str(random.randint(2**32, 2**33)) + str(random.randint(2**32, 2**33))) * 13 + random.randint(2**32, 2**33)










