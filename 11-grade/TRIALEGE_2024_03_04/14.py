alpha = '0123456789a'

for x in alpha:
  if (int(f'982{x}8', 11) + int(f'194{x}7', 11)) % 58 == 0:
    print( (int(f'982{x}8', 11) + int(f'194{x}7', 11)) / 58)
