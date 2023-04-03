for m in range(256):
      for x3 in range(m):
        num = 15 * 2 + 35 * 3 + x3 * 2
        dev = [ x for x in range(1, num // 2 + 1) if num % x == 0 ]
        if len(dev) == 4:
          print(m, num)

# 246 (625)
