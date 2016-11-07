# -*- coding: utf-8 -*-
import time


def timer(f):
    def init(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        print 'Execution time {} was : {}'.format(f.__name__, end_time - start_time)
        return result
    return init


@timer
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


@timer
def fact_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


@timer
def fact_recurs_dec(n):
    return 1 if n == 0 else n * fact_recurs(n - 1)


def fact_recurs(n):
    return 1 if n == 0 else n * fact_recurs(n - 1)


if __name__ == '__main__':
    for _ in range(1):
        number = 996
        print fact(number)
        print fact_reduce(number)
        print fact_recurs_dec(number)
        print '-----------------------------------------------------------------------------------'
