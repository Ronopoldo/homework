alpha = '01234567890A'

answers = []

for x in alpha:
    for y in alpha:
        num = int(f'{x}341{y}',11) + int(f'56{x}1{y}', 19)
        if num % 305 == 0:
            answers.append(num)


print(min(answers) // 305)

#2778

# 64
# 3263
# 62