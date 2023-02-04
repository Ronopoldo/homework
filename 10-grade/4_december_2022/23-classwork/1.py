# ГЕОМЕТРИЧЕСКАЯ ПРОГРЕССИЯ
def sumOfProgression(b1, q, n):
    if q != 1:
        return (b1 * (q ** n - 1)) / (q - 1)
    else:
        return b1 * n


# print(sumOfProgression(2, 3, 4))
print(sumOfProgression(int(input('Введите b₁\n')), int(input('Введите q\n')), int(input('Введите n\n'))))
