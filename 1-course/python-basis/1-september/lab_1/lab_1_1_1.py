def virusDeleter(s, v):
    while v.upper() in s.upper():
        virusIndex = s.upper().index(v.upper())
        virusInString = s[virusIndex: virusIndex + len(v)]
        s = s.replace(virusInString, '')

    return s


s = str(input())  # Исходная строка
v = str(input())  # Вирус

print(virusDeleter(s, v))
