# -*- coding: utf-8 -*-
import os
import sys


def fiban(n):
    first = 1
    second = 1
    for i in range(1, n):
        first, second = second, first + second
    return first


def write_fibanfile(inputf, n):
    first = 1
    second = 1
    with open(inputf, 'w') as input_file:
        for i in range(1, n):
            input_file.write(str(first) + ', ')
            first, second = second, first + second
        input_file.write(str(first))

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
