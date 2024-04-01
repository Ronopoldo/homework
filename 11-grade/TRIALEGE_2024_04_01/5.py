def sumOfDigits(num):
    strNum = str(num)
    output = 0
    for letter in strNum:
        output+=int(letter)
    return output

for N in range(4096):
    N2 = bin(N)[2::]

    N2 = N2 + str(sumOfDigits(N2) % 2)
    N2 = N2 + str(sumOfDigits(N2) % 2)

    if int(N2, 2) > 154:
        print(int(N2, 2), N)