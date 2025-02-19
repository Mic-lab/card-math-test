from math import comb as c, factorial

def fail(*args):
    i = len(args)

    n = 52 - 13*i
    k = 8 - sum(args)
    return ( c(n, k) * c(13, args[-1]) )

def f(a, b, c_, d):
    return c(13, a) * c(13, b) * c(13, c_) * c(13, d)

def p_start_hand(a, b, c_, d):
    product = 1
    for i in (a, b, c_, d):
        product *= c(13, i)
    return product / c(52, 8) * 100

def p_start_hand_wlog(a, b, c_, d):
    return p_start_hand(a, b, c_, d) * factorial(4)

def p_a(start_a, a):
    discards = min(5, 8-start_a)
    # discards = 5
    # print(discards, 'd')
    if discards - a < 0:
        return 0
    return (c(13-start_a, a) * c(52 - 8 - (13 - start_a), discards - a)) / c(52 - 8, discards)

def product(range_, func):
    p = 1
    for n in range_:
        print(f'{func(n)=}')
        p *= func(n)
    return p

def p_duplicates(x):
    return x
    # return product(range(x-2), lambda n: (13 - 2 - n) / (52 - 2 - n)) * product(range(x + 1, 9), lambda n: (13 * 3 - (n - (x + 1) )) / (52 - 2 - n) )

def p_duplicates(x):

mode = 'a 4'

if mode == 'a 4':
    data = {}
    
    for x in range(3, 9):
        val = p_duplicates(x) * 100
        data[x] = val
        print(f'    P({x}) CARDS = {val} %')
        print('\n')

    keys = list(reversed(list(data.keys())))
    for i in range(len(keys)):
        
        p_sum = 0
        for j in range(i + 1):
            key_2 = keys[j]
            p_sum += data[key_2]

        print(p_sum)
            


elif mode == 'a 3':
    # a, b, c_, d = 2, 2, 2, 2
    a, b, c_, d = 3, 1, 2, 2
    # a, b, c_, d = 0, 0, 0, 8
    print(f'{factorial(4)}')
    print(p_start_hand(a, b, c_, d))
    print(p_start_hand_wlog(a, b, c_, d))

elif mode == 'a 2':
    for start_a in range(9):
        print(start_a)
        # start_a = 0

        s = 0
        for i in range(6):
            prob_a = p_a(start_a, i)
            # print(f'\nwith {start_a} A\'s, odds of getting {i} A is:')
            print(prob_a)
            s += prob_a
        print()
        # print(s)

elif mode == 'a 1':
    d = {}

    for i in range(9):
        d[i] = 0

    for i in range(9):
        for j in range(9):
            for k in range(9):
                for l in range(9):
                    if i + j + k + l == 8:
                        val = 1
                        val = f(i, j, k, l)
                        d[i] += val
                        d[j] += val
                        d[k] += val
                        d[l] += val

    print(d)
