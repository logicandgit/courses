# -*- coding: utf-8 -*-
import os
import sys


def copy_second_line(inputf, outputf):
    with open(inputf) as input_file, open(outputf, 'w') as output_file:
        pos = 1
        for line in input_file:
            if pos % 2 == 0:
                output_file.write(line)
            pos += 1

if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            raise Exception('Need two argument, path to files')

        input_file_path, out_file_path = sys.argv[1:3]

        if not os.path.exists(input_file_path):
            raise Exception('File is absent by path: {}'.format(input_file_path))
        # input_file_path = 'b.txt'
        # out_file_path = 'c.txt'
        copy_second_line(input_file_path, out_file_path)

    except Exception, err:
        print(err.message)

