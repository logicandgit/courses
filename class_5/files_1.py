# -*- coding: utf-8 -*-
import sys
import os


def read_file(inputf):
    with open(inputf) as input_file:
        print(input_file.read())

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise Exception('Need one argument, path to file')

        file_path = sys.argv[1]
        if not os.path.exists(file_path):
            raise Exception('File is absent by path: {}'.format(file_path))

        read_file(file_path)
    except Exception, err:
        print(err.message)
