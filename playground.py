from math import comb as c

def P1(x, y):
    n = min(5, 8-x)

    if n-y < 0:
        return 0

    return c(13-x, y)*c(31+x, n-y) / c(47, n)

    
for y in range(9):
    for x in range(9):
        ans = P1(x, y)
        # print(round(ans, 4), end='\t')
        print(ans, end='\t')
    print()
