from math import comb

def p_exacte(a, b, c, d):
    # NOTE: comb est la fonction combinaison
    return (comb(13, a) * comb(13, b) * comb(13, c) * comb(13, d)) / comb(52, a + b + c + d)

def p0_exacte(x):

    sum_ = 0

    # a, b, c, d prenne tous les permutations possibles entre les entiers de 0 à 8
    # (9 à été écrite car les boucles sont exclusives)
    # Alors, condition (2) est satisfaite
    for a in range(9):
        for b in range(9):
            for c in range(9):
                for d in range(9):
                    
                    # Assure que condition (1) et condition (3) sont satisfaites
                    if a + b + c + d == 8 and max(a, b, c, d) == x:
                        sum_ += p_exacte(a, b, c, d)

    return sum_

def p_1r_exacte(y, x):
    r = min(5, 8-x)
    if y == 6:
        print(r, '<<<')
    if r - y < 0:
        return 0

    return comb(13 - x, y) * comb(31 + x, r - y) / comb(44, r)

print(end='\t')
for x in range(9):
    print(x, end='\t')
print()
for y in range(7):
    print(y, end='\t')
    for x in range(9):
        # print(f'{p_1r_exacte(y, x):.4f}', end='\t')
        print(f'{p_1r_exacte(y, x)}', end='\t')
        # print((x, y), end='\t')
    print()

