from fnmatch import fnmatch 
i = 0

for i in range(0,30000,2024):
  if fnmatch(str(i), '3?6906*4'):
    print(i)

for i in range((300_000 // 2024) * 2024 ,400000,2024):
  if fnmatch(str(i), '3?6906*4'):
    print(i)  

for i in range((3_000_000 // 2024) * 2024 ,4_000_000,2024):
  if fnmatch(str(i), '3?6906*4'):
    print(i)  

for i in range((30_000_000 // 2024) * 2024 ,40_000_000,2024):
  if fnmatch(str(i), '3?6906*4'):
    print(i)  

for i in range((300_000_000 // 2024) * 2024 ,400_000_000,2024):
  if fnmatch(str(i), '3?6906*4'):
    print(i)  

for i in range((3000_000_000 // 2024) * 2024 ,4000_000_000,2024):
  if fnmatch(str(i), '3?6906*4'):
    print(i)  