from math import comb as c

def fail(*args):
    i = len(args)

    n = 52 - 13*i
    k = 8 - sum(args)
    return ( c(n, k) * c(13, args[-1]) )

def f(a, b, c_, d):
    return c(13, a) * c(13, b) * c(13, c_) * c(13, d)

def p(a, b, c_, d):
    return p(a, b, c_, d) / c(52, 8)

def p_a(start_a, a):
    discards = min(5, 8-start_a)
    # discards = 5
    # print(discards, 'd')
    if discards - a < 0:
        return 0
    return (c(13-start_a, a) * c(52 - 8 - (13 - start_a), discards - a)) / c(52 - 8, discards)

mode = 'attempt 2'

if mode == 'attempt 2':
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

elif mode == 'attempt 1':
    d = {}

    for i in range(9):
        d[i] = 0

    for i in range(9):
        for j in range(9):
            for k in range(9):
                for l in range(9):
                    if i + j + k + l == 8:
                        v = 1
                        v = f(i, j, k, l)
                        d[i] += v
                        d[j] += v
                        d[k] += v
                        d[l] += v

    print(d)
