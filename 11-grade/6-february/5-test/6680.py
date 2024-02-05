s = open('6680.txt').read()

prohibidedAlpha = '#&%GHIJKLMNOPQRSTUVWXYZ'


def isColor(clearStr):
    for letta in clearStr:
        if letta in prohibidedAlpha:
            return False

    return True


def leadingColorRed(clearStr):
    if len(clearStr) != 6:
        return None
    red = clearStr[0:2]
    blue = clearStr[2:4]
    green = clearStr[4:6]
    palitre = [int(red, 16), int(blue, 16), int(green, 16)]
    if (max(palitre) == int(red, 16)) and (palitre.count(int(red, 16)) == 1):
        return True
    else:
        return False


redCounter = 0

for i in range(len(s) - 7):
    if s[i] == '#':
        if isColor(s[i + 1:i + 7]):
            if leadingColorRed(s[i + 1:i + 7]):
                redCounter += 1

print(redCounter)
