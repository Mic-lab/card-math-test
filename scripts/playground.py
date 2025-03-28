from math import comb as c

def P1(x, y):
    r = min(5, 8-x)

    if r-y < 0:
        return 0

    # return c(13-x, y)*c(31+x, r-y) / c(47, r)
    c_des = 13-x
    c_des_tir = y
    c_indes = 31 + x
    c_indes_tir = r-y
    c_restants = 44
    c_restants_tir = r
    print(f'{c_des=}')
    print(f'{c_des_tir=}')
    print(f'{c_indes=}')
    print(f'{c_indes_tir=}')
    print(f'{c_restants=}')
    print(f'{c_restants_tir=}')

    return c(13-x, y)*c(31+x, r-y) / c(44, r)
    # return c(13-x, y)*c(39-(r-y), r-y) / c(44, r)

def P2(x, y, z):
    r = min(5, 8-x-y)

    if r-z< 0:
        return 0

    # bad_cards = 39 - min(5, 8-x) - r
    bad_cards = 39 - (8 - x) - min(5, 8-x) + y
    print(f'{(8 - x)=}')
    print(f'{min(5, 8-x) - y=}')

    # print()
    # print((x, y, z), f'{bad_cards=}', f'r0={8-x}', f'r1={min(5, 8-x)}', f'r2={r}')




    c_des = 13-x-y
    c_des_tir = z
    c_indes = bad_cards
    c_indes_tir = r-z
    c_restants = 44 - min(5, 8-x)
    c_restants_tir = r
    print(f'{c_des=}')
    print(f'{c_des_tir=}')
    print(f'{c_indes=}')
    print(f'{c_indes_tir=}')
    print(f'{c_restants=}')
    print(f'{c_restants_tir=}')
    return c(13-y-x, z)*c(bad_cards, r-z) / c(44 - min(5, 8-x), r)



# print(P1(2, 4))
# print(P2(2, 1, 2), (2,1,2))
# print(P2(4, 0, 4), (4,0,4))
print(P2(2, 2, 1), (2,2,1))
    
# for y in range(9):
#     for x in range(9):
#         ans = P1(x, y)
#         print(ans, end='\t')
#     print()


# COORDS = ((2,0),(3,0),(4,0),(2,1),(3,1),(2,2))
# # COORDS = ((3,1), )
#
# for z in range(7):
#     # print(z)
#     for coord in COORDS:
#         x, y = coord
#         print(P2(x, y, z), end='\t')
#     print()

'''
suppose you choose 8 cards from a deck of 52
the most repeated suit is repeated x times
you then remove as many cards from your hand as possible without discarding the most repeated suit,
but you cants remove more then 5 cards. hence, you remove r_1 cards from your hand of 8; r1=min(5, 8-x)
you draw r_1 cards from the deck
you have now gained y cards of the same suit of x.
you again, remove r_2 cards from your hand of 8; r_2=min(5, 8-x-y)
you have now gained z cards
what are the odds of gaining z cards, given x and y?
'''
