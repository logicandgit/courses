def sum_mul(n):
    summa = 0
    mult = 1
    _res = n
    while _res > 0:
        _res, res = divmod(_res, 10)
        summa += res
        mult *= res
    return summa, mult

if __name__ == '__main__':
    print(sum_mul(59))
