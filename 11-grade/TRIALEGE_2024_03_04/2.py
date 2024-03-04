              from itertools import *
              def f(x, y, z, w):
                  return ((y <= z) or (not(x) and w)) == (w == z)

              for t in product([0, 1], repeat=4):
                  table = [(t[0], 1, 0, 0),
                           (0,0,0,1),
                           (0,1,t[1],t[2])
                           ]
                  if len(table) == len(set(table)):
                      for p in permutations('xyzw'):
                          if [f(**dict(zip(p, r))) for r in table] == [1, 1 , 1]:
                              print(p)











                #17) 180 190360573
                # 9) 941
                # 8) 293 601 280
                # 24) 544