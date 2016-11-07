# -*- coding: utf-8 -*-
import sys


def fiban(n):
    res = [1, 1]
    for i in range(1, n-1):
        res.append(res[i-1] + res[i])
    return res


def write_fibanfile(inputf, n):
    with open(inputf, 'w') as input_file:
        input_file.write(', '.join(str(x) for x in fiban(n)))

if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            raise Exception('Need two argument: path to file and n-th member Fibonacci numbers')

        file_path = sys.argv[1]
        number_fib = sys.argv[2]

        if not number_fib.isdigit():
            raise Exception('Second arg must be number')

        write_fibanfile(file_path, int(number_fib))
        print(fiban(int(number_fib)))
    except Exception, err:
        print(err.message)
