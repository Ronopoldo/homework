# (x ∧ y ∧¬z) ≡ (y ∨ z ∨ ¬w)

print('w y z x     F')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range (2):
                if ((x and y and (not z)) == (y or z or (not w))):
                    print(w, y, z, x, '   ' , int((x and y and (not z)) == (y or z or (not w))))


# (W) (Y) (Z) (X)
# wyzx