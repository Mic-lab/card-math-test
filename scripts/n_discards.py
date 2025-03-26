from itertools import combinations, product
from math import comb as c

def r(i, *args):
    print(f'r{i}, {args}')
    # print(f'r({i})')
    cards_to_remove = 8
    for j in range(i+1):
        cards_to_remove -= args[j]
        print(args[j])
        # print(f'\t-{args[j]}')
    # print(f'\tr({i}) = min(5, {cards_to_remove})')
    return min(5, cards_to_remove)


def p_start(a, b, c_, d):
    # NOTE: comb est la fonction combinaison
    return (c(13, a) * c(13, b) * c(13, c_) * c(13, d)) / c(52, a + b + c_ + d)

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
                        sum_ += p_start(a, b, c, d)

    return sum_

def p_flush(n):
    odds = 0
    possible_args = list(product(range(9), repeat=n))
    # print(possible_args)
    for args in possible_args:
        # restriction 1
        if sum(args[:-1]) >= 5:
            continue
        # rest 2
        elif sum(args) < 5:
            continue
        

        added_odds = p_inconditionelle(*args)
        odds += added_odds
        # if added_odds != 0:
        #     print('Adding', args, added_odds * 100, '%')
    return odds


def p_inconditionelle(*args):
    product_ = 1
    for i in range(len(args)):
        # print(f'\t{product_*100=}')
        product_ *= p_exacte(*args[:i+1])
        # print(f'\t times {p_exacte(*args[:i+1]) * 100} ({args[:i+1]})')
        # print(f'\t new : {product_}')

    if product_ != 0:
        # print(f'--- [p_inconditionelle] {args} ---')
        # print(args, product_ * 100)
        # print('adding', args, product_ * 100)
        pass
    return product_

def p_exacte(*args):
    # print(f'[p_exacte {args}]')
    n = len(args)

    # if n == 1 and False:
    if n == 1:
        ans = p0_exacte(args[0])

    else:
        cartes_desirees = 13
        for i in range(1, n):
            cartes_desirees -= args[i-1]

        cartes_desirees_tirees = args[-1]

        # print('----')
        cartes_indesirees = 39
        for i in range(1, n):


            if i == 1:
                cartes_indesirees -= 8 - args[i - 1]
                # print(f'minus {8 - args[i - 1]}')
                # print()
            else:
                # minus not plus!!!! > v <
                # cartes_indesirees -= r(i-1, *args) - args[i-1]

                subtract = r(i-2, *args) - args[i-1]
                # print(f'minus {subtract}')
                cartes_indesirees -= subtract
                #or print(f'vv is r({i-1})')
        # print('----')

        # print(r(n-1, *args), '<')

        cartes_indesirees_tirees = r(n-2, *args) - args[-1]
        print(args, n-2, r(n-2, *args))

        cartes_restants = 52
        for i in range(1, n):
            if i == 1:
                cartes_restants -= 8
            else:
                cartes_restants -= r(i-2, *args)

        # cartes_restants_tirees = r(n - 1, *args)
        cartes_restants_tirees = r(n - 2, *args)


        if cartes_indesirees_tirees < 0:
            return 0
        else:
            pass


        ans = c(cartes_desirees, cartes_desirees_tirees) * c(cartes_indesirees, cartes_indesirees_tirees) / c(cartes_restants, cartes_restants_tirees)

        # print(f'\t{cartes_desirees=}')
        # print(f'\t{cartes_desirees_tirees=}')
        # print(f'\t{cartes_indesirees=}')
        # print(f'\t{cartes_indesirees_tirees=}')
        # print(f'\t{cartes_restants=}')
        # print(f'\t{cartes_restants_tirees=}')
        # print(f'\tp exacte (2, 4) = {ans * 100} %')

    return ans

# print(p_inconditionelle(3, 2))


# print(p_exacte(2,1,2))
# print(p_exacte(4,0,4))
# print(p_exacte(2,2,1))
# print(p_exacte(2))

for i in range(9):

    # if i == 3:
    print(f'\nFinal answer {i}:', p_flush(i) * 100)
