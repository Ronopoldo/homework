def div(x):
    counter = 0
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0 and ((x // i) - i <= 100) :
            counter+=1
    return counter

answers = []

for num in range(1_000_000, 2_000_001):
    if div(num) >= 3:
        answers.append(num)
        print('GOTCHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    print(num, div(num), answers)

print(answers)