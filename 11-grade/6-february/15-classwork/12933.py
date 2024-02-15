s = open('26_12933.txt').read().split('\n')[1:] #997 500

timeline = [0 for i in range(len(s) - 1)]
# ШЛИФОВКА ОКРАСКА
separated = [[0, 0, 'N/A', 0] for i in range(len(s) - 1)]

for i in range(len(s) - 1):
  if min(int(s[i].split( )[0]), int(s[i].split( )[1])) == int(s[i].split( )[0]):
    temp = 'Ш'
  else:
    temp = 'О'
    
  separated[i] = [min(int(s[i].split( )[0]), int(s[i].split( )[1])), max(int(s[i].split( )[0]), int(s[i].split( )[1])), temp, i + 1]

separated = sorted(separated)

tempBeg = 0
tempEnd = 0 

for i in range(len(separated)):
  if separated[i][2] == 'Ш':
    timeline[tempBeg] = separated[i][3]
    tempBeg+=1
  else:
    timeline[-tempEnd] = separated[i][3]
    tempEnd+=1

print(tempBeg, timeline[500])

#489 920